"""World component."""

from .base import Base
from . import validate
from math import tau


class World(Base):
    """Representation of a world."""

    def __init__(self, moniker: str, semi_major_axis: float, inv_flattening: float, rotation_rate: float) -> None:
        r"""
        Initialize world.

        :param moniker: Name of the World.
        :type moniker: str

        :param semi_major_axis: Semi major axis of the world :math:`(a)`,
        :type semi_major_axis: float

        :param inv_flattening: Inverse flattening of the world :math:`(f^{-1})`
        :type inv_flattening: float

        :param rotation_rate: Rotation rate of the world :math:`(\omega_{ie})`, rad/s
        :type rotation_rate: float
        """
        super().__init__(moniker)
        self.a = semi_major_axis
        f = 1 / inv_flattening
        self.e2 = f * (2 - f)
        self.omega_ie = rotation_rate

    @property
    def a(self):
        """Semi-major-axis getter."""
        return self._a

    @a.setter
    def a(self, value):
        """Semi-major-axis setter."""
        validate.number(value, minvalue=0.0)
        self._a = value

    @property
    def omega_ie(self):
        """Rotation rate getter."""
        return self._omega_ie

    @omega_ie.setter
    def omega_ie(self, value):
        """Rotation rate setter."""
        validate.number(value, minvalue=0.0, maxvalue=tau)
        self._omega_ie = value
