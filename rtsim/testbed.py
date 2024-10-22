"""Testbed component."""

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
import numpy as np


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
        if not isinstance(obj, dict):
            raise TypeError

        for axis in obj:
            validate.component(obj[axis], Axis)

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

        for a in self.axes:
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
