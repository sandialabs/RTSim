"""Axis component."""

from .base import Base
from .exceptions import FrameTypeError
from .frame import Frame
from .pva import ConstantPVA, TimePVA
import numpy as np


class Axis(Base):
    """Representation of a rotational testbed axis."""

    def __init__(self, moniker: str, zeta: Frame) -> None:
        r"""
        Initialize axis.

        :param moniker: Name of the axis.
        :type moniker: str

        :param zeta: Zero frame of the axis.
        :type zeta: Frame[Fixed]

        :raises FrameTypeError: If the zero :math:`(\zeta)` coordinate frame type is not 'Fixed'.
        """
        super().__init__(moniker)

        if zeta.frame_type != "Fixed":
            var_name = "zeta"
            raise FrameTypeError(var_name, "Fixed")

        self.zeta = zeta

    def process(
        self, mu: Frame, rho: Frame, alpha: ConstantPVA | TimePVA, omega: ConstantPVA | TimePVA
    ) -> tuple[TimePVA, TimePVA]:
        r"""
        Process the axis to provide linear and angular PVA outputs of axis.

        :param mu: Axis misalignment :math:`(\mu)` coordinate frame.
        :type mu: Frame[Full]

        :param rho: Axis rotating :math:`(\rho)` coordinate frame.
        :type rho: Frame[Rotating]

        :param alpha: Linear PVA from lower level axis.
        :type alpha: ConstantPVA | TimePVA

        :param omega: Angular PVA from lower level axis.
        :type omega: ConstantPVA | TimePVA

        :raises FrameTypeError: If 'mu' is not a Full type coordinate frame.
        :raises FrameTypeError: If 'rho' is not a Rotating type coordinate frame.

        :return: Linear and angular PVA from this axis.
        :rtype: tuple[TimePVA, TimePVA]
        """
        if mu.frame_type != "Full":
            var_name = "mu"
            raise FrameTypeError(var_name, "Full")

        self.mu = mu

        if rho.frame_type != "Rotating":
            var_name = "rho"
            raise FrameTypeError(var_name, "Rotating")

        self.rho = rho

        C_dot_rho = self.rho.Omega @ self.rho.C
        C_ddot_rho = self.rho.Omega_dot @ self.rho.C + self.rho.Omega @ self.rho.Omega @ self.rho.C

        alpha_a = self.zeta.C @ (
            self.mu.linear.a + C_ddot_rho @ alpha.p + 2 * C_dot_rho @ alpha.v + self.rho.C @ alpha.a
        )

        alpha_v = self.zeta.C @ (self.mu.linear.v + C_dot_rho @ alpha.p + self.rho.C @ alpha.v)

        alpha_p = self.zeta.linear.p + self.zeta.C @ (self.mu.linear.p + self.rho.C @ alpha.p)

        omega_a = self.zeta.C @ (
            self.mu.angular.a
            + self.mu.Omega @ self.mu.C @ self.rho.angular.v
            + self.mu.C @ self.rho.angular.a
            + self.mu.Omega @ self.mu.C @ self.rho.C @ omega.v
            + self.mu.C @ self.rho.Omega @ self.rho.C @ omega.v
            + self.mu.C @ self.rho.C @ omega.a
        )

        omega_v = self.zeta.C @ (self.mu.angular.v + self.mu.C @ self.rho.angular.v + self.mu.C @ self.rho.C @ omega.v)

        return (
            TimePVA(p=alpha_p, v=alpha_v, a=alpha_a),
            TimePVA(p=np.zeros((omega_v.shape[0], 3, 1)), v=omega_v, a=omega_a),
        )
