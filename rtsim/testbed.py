"""
RTSim Testbed component.

Copyright © 2024, National Technology & Engineering Solutions of
Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with
NTESS, the U.S. Government retains certain rights in this software.
"""

# SPDX-License-Identifier: BSD-3-Clause

from .axis import Axis
from .base import Base
from .body import Body
from .exceptions import AxisCountError
from .pva import ConstantPVA
from .frame import Frame
from .mount import Mount
from .world import World
from . import validate
from math import tau
import matplotlib.pyplot as plt
import numpy as np

plt.rc("text", usetex=True)
plt.rc(
    "text.latex",
    preamble="\n".join([r"\usepackage{siunitx}", r"\usepackage{amsmath}", r"\DeclareSIUnit{\gravity}{\textsl{g}}"]),
)


class Testbed(Base):
    """Representation of a rotational testbed."""

    def __init__(
        self,
        moniker: str,
        llhg: tuple[float, float, float, float],
        components: tuple[World, dict[int, Axis], Mount, Body],
    ) -> None:
        """
        Initialize testbed.

        :param moniker: Name of the testbed.
        :type moniker: str

        :param llhg: Latitude, Longitude and Height above ellipsiod of testbed, and value of gravity at
                     testbed location.
        :type llhg: tuple[float, float, float, float]

        :param components: Components of the testbed (World, Rotating Axes, Mount and Body)
        :type components: tuple[World, dict[Axis], Mount, Body]
        """
        super().__init__(moniker)

        self.lat, self.lon, self.hae, self.g = llhg

        self.world, self.axes, self.mount, self.body = components

        phi = np.radians(self._lat)
        lam = np.radians(self._lon)
        sin_phi = np.sin(phi)
        cos_phi = np.cos(phi)
        sin_lam = np.sin(lam)
        cos_lam = np.cos(lam)

        M_phi = self.world.a / np.sqrt(1 - self.world.e2 * sin_phi**2)

        self.nav = Frame(
            ConstantPVA(
                p=np.array(
                    [
                        [(M_phi + self._hae) * cos_phi * cos_lam],
                        [(M_phi + self._hae) * cos_phi * sin_lam],
                        [(M_phi * (1 - self.world.e2) + self._hae) * sin_phi],
                    ]
                ),
                v=np.zeros((3, 1)),
                a=np.zeros((3, 1)),
            ),
            ConstantPVA(p=np.array([[0.0], [-(tau / 4 + phi)], [lam]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
        )

    @property
    def lat(self):
        """Latitude."""
        return self._lat

    @lat.setter
    def lat(self, value):
        validate.number(value, -90, 90)
        self._lat = value

    @property
    def lon(self):
        """Longitude."""
        return self._lon

    @lon.setter
    def lon(self, value):
        validate.number(value, -180, 180)
        self._lon = value

    @property
    def hae(self):
        """Height above ellipsoid."""
        return self._hae

    @hae.setter
    def hae(self, value):
        validate.number(value)
        self._hae = value

    @property
    def g(self):
        """Local gravity."""
        return self._g

    @g.setter
    def g(self, value):
        validate.number(value, 0.0)
        self._g = value

    @property
    def world(self):
        """World component."""
        return self._world

    @world.setter
    def world(self, obj):
        validate.component(obj, World)
        self._world = obj

    @property
    def axes(self):
        """Axes components."""
        return self._axes

    @axes.setter
    def axes(self, obj):
        if not isinstance(obj, list):
            raise TypeError

        for axis in obj:
            validate.component(axis, Axis)

        self._axes = obj

    @property
    def mount(self):
        """Mount component."""
        return self._mount

    @mount.setter
    def mount(self, obj):
        validate.component(obj, Mount)
        self._mount = obj

    @property
    def body(self):
        """Mount component."""
        return self._body

    @body.setter
    def body(self, obj):
        validate.component(obj, Body)
        self._body = obj

    def process(self, time: np.ndarray, misalignments: dict[int, Frame], rotations: dict[int, Frame]) -> None:
        """
        Process testbed inputs into body inputs.

        :param time: Relative time of each step.
        :type time: np.ndarray

        :param misalignments: Misalignment coordinate frame of each testbed axis.
        :type misalignments: list[Frame[Full]]

        :param rotations: Rotating coordinate frame of each testbed axis.
        :type rotations: list[Frame[Rotating]]
        """
        if len(misalignments) != len(self._axes):
            raise AxisCountError(len(self._axes), "misalignment")
        if len(rotations) != len(self._axes):
            raise AxisCountError(len(self._axes), "rotations")

        self.time = time
        self.world.process(self.time)

        alpha = ConstantPVA(
            p=self.mount.frame.linear.p + self.mount.frame.C @ self.body.frame.linear.p,
            v=np.zeros((3, 1)),
            a=np.zeros((3, 1)),
        )

        omega = ConstantPVA(p=np.zeros((3, 1)), v=np.zeros((3, 1)), a=np.zeros((3, 1)))

        Cib = self.mount.frame.C @ self.body.frame.C

        for a in range(len(self.axes)):
            alpha, omega = self.axes[a].process(misalignments[a], rotations[a], alpha, omega)
            Cib = self.axes[a].zeta.C @ self.axes[a].mu.C @ self.axes[a].rho.C @ Cib

        Cin = self.world.frame.C @ self.nav.C
        Cib = Cin @ Cib

        self.aaiib = self.world.frame.Omega @ Cin @ omega.v + Cin @ omega.a
        self.aviib = self.world.frame.angular.v + Cin @ omega.v

        self.laiib = (
            self.world.frame.Omega @ self.world.frame.Omega @ self.world.frame.C @ self.nav.linear.p
            + self.world.frame.Omega @ self.world.frame.Omega @ Cin @ alpha.p
            + 2 * self.world.frame.Omega @ Cin @ alpha.v
            + Cin @ alpha.a
        )

        self.sfiib = self.laiib + Cin @ np.array([[0.0], [0.0], [-self.g]])

        Cbi = np.transpose(Cib, (0, 2, 1))

        self.avbib = Cbi @ self.aviib
        self.aabib = Cbi @ self.aaiib
        self.labib = Cbi @ self.laiib
        self.sfbib = Cbi @ self.sfiib

    def plot(self, *, variable="la", frame="b", separate=False) -> None:
        """
        Plot the processed results.

        :param variable: The variable to be plotted.
            options:
                "la" for linear acceleration
                "aa" for angular acceleration
                "av" for angular velocity
                "sf" for specific force
            defaults to "la"
        :type variable: str, optional

        :param frame: Reference frame of variable.
            options:
                "i" for inertial frame
                "b" for body frame
            defaults to "b"
        :type frame: str, optional

        :param separate: Separate x, y, and z axis into subplots (True, False), defaults to False
        :type separate: bool, optional
        """
        axs = ["x", "y", "z"]

        var_info = {
            "la": {"unit": r"\gravity", "sym": r"\boldsymbol{a}"},
            "sf": {"unit": r"\gravity", "sym": r"\boldsymbol{f}"},
            "av": {"unit": r"\radian/\second", "sym": r"\boldsymbol{\omega}"},
            "aa": {"unit": r"\radian/\second\squared", "sym": r"\dot{\boldsymbol{\omega}}"},
        }

        x = np.round(vars(self)[f"{variable}{frame}ib"].copy(), 12)
        x /= 1 if variable[0] == "a" else self.g
        exp, mdf = unit_modifier(x)

        ustr = "".join([r"\unit{", f"{mdf}{var_info[variable]['unit']}", r"}"])

        title = "".join(
            ["$", f"{var_info[variable]['sym']}", r"^\mathrm{", f"{frame}", r"}_{\mathrm{i}\mathrm{b}}$, ", f"{ustr}"]
        )

        if separate:
            fig, ax = plt.subplots(3, 1, sharex=True, figsize=(6.5, 8.0))

            for a in range(3):
                ax[a].plot(self.time, x[:, a].flatten() * 10**exp)
                ax[a].set(ylabel=f"{axs[a]}")
                ax[a].grid(visible=True, which="both", linestyle=":", alpha=0.25)

            ax[0].set(title=title)
            ax[2].set(xlabel=r"Time, \unit{\second}")
            fig.align_ylabels(ax)
            fig.subplots_adjust(left=0.10, bottom=0.12, right=0.96, top=0.94, wspace=0.0, hspace=0.0)
        else:
            fig, ax = plt.subplots(1, 1, figsize=(6.50, 4.02))

            for a in range(3):
                ax.plot(self.time, x[:, a].flatten() * 10**exp, label=f"{axs[a]}")

            ax.set(xlabel=r"Time, \unit{\second}", ylabel=title)
            ax.grid(visible=True, which="both", linestyle=":", alpha=0.25)
            ax.spines[:].set_visible(False)
            ax.legend(frameon=False)
            fig.subplots_adjust(left=0.10, bottom=0.12, right=0.96, top=0.94)


def unit_modifier(x: np.ndarray):
    """Modify units of varable."""
    mods = {
        -24: r"\yotta",
        -21: r"\zetta",
        -18: r"\exa",
        -15: r"\peta",
        -12: r"\tera",
        -9: r"\giga",
        -6: r"\mega",
        -3: r"\kilo",
        0: r"",
        3: r"\milli",
        6: r"\micro",
        9: r"\nano",
        12: r"\pico",
        15: r"\femto",
        18: r"\atto",
        21: r"\zepto",
        24: r"\yocto",
    }

    exp = np.arange(-24.0, 25.0, 3.0)
    xm = max(abs(x.flatten()))

    if xm == 0.0:
        return 0, r""

    xma = xm * 10**exp
    idx = np.where(xma > 1.0)[0][0]

    return exp[idx], mods[exp[idx]]
