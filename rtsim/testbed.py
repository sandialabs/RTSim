"""Testbed component."""

from .axis import Axis
from .base import Base
from .body import Body
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
        components: tuple[World, list[Axis], Mount, Body],
    ) -> None:
        """
        Initialize testbed.

        :param moniker: Name of the testbed.
        :type moniker: str

        :param llhg: Latitude, Longitude and Height above ellipsiod of testbed, and value of gravity at
                     testbed location.
        :type llhg: tuple[float, float, float, float]

        :param components: Components of the testbed (World, Rotating Axes, Mount and Body)
        :type components: tuple[World, list[Axis], Mount, Body]
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
