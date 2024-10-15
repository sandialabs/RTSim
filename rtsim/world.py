"""World component."""

from . import validate
from .base import Base
from .frame import Frame
from .pva import ConstantPVA, TimePVA
from math import tau
import numpy as np


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
        """Semi-major-axis."""
        return self._a

    @a.setter
    def a(self, value):
        validate.number(value, minvalue=0.0)
        self._a = value

    @property
    def omega_ie(self):
        """Rotation rate."""
        return self._omega_ie

    @omega_ie.setter
    def omega_ie(self, value):
        validate.number(value, minvalue=0.0, maxvalue=tau)
        self._omega_ie = value

    def process(self, time: np.ndarray) -> None:
        """
        Compute world coordinate frame parameters for all input time steps.

        :param time: Relative time of each step.
        :type time: np.ndarray
        """
        steps = time.size
        omega = np.zeros((steps, 3, 1))
        omega[:, 2, 0] = self._omega_ie

        theta = np.zeros((steps, 3, 1))
        theta[:, 2, 0] = omega[:, 2, 0] * time

        self.frame = Frame(
            ConstantPVA(p=np.zeros((3, 1)), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
            TimePVA(p=theta, v=omega, a=np.zeros((steps, 3, 1))),
        )

        self.frame.C = np.transpose(self.frame.C, (0, 2, 1))
