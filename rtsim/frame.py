"""RTSim coordinate frames."""

from .exceptions import PVATypeError
from .pva import ConstantPVA, TimePVA
import numpy as np


class Frame:
    """RTSim coordinate Frame class."""

    def __init__(self, linear: ConstantPVA | TimePVA, angular: ConstantPVA | TimePVA) -> None:
        """
        Initialize a frame.

        :param linear: Linear PVA of the frame.
        :type linear: ConstantPVA | TimePVA

        :param angular: Angular PVA of the frame.
        :type angular: ConstantPVA | TimePVA

        :raises PVATypeError: If either 'linear' or 'angular' are not ConstantPVA nor TimePVA.
        """
        type_test = np.array(
            [
                [isinstance(linear, ConstantPVA), isinstance(angular, ConstantPVA)],
                [isinstance(linear, ConstantPVA), isinstance(angular, TimePVA)],
                [isinstance(linear, TimePVA), isinstance(angular, ConstantPVA)],
                [isinstance(linear, TimePVA), isinstance(angular, TimePVA)],
            ]
        )

        bad_type = ~type_test.any(axis=0)
        if bad_type.any():
            raise PVATypeError(["linear", "angular"][np.where(bad_type)[0][0]])

        self.frame_type = ["Fixed", "Rotating", "Translocating", "Full"][np.where(type_test.all(axis=1))[0][0]]

        self.linear = linear
        self.angular = angular

        self.C = orientation_to_dcm(self.angular.p)
        self.Omega = skew_symetric(self.angular.v)
        self.Omega_dot = skew_symetric(self.angular.a)

    def __str__(self):
        """Return a string representation of the coordinate frame."""
        return f"{self.frame_type} Coordinate Frame"

    def __repr__(self):
        """Return a string representation of the coordinate frame."""
        return f"{self.frame_type} Coordinate Frame"


def orientation_to_dcm(v: np.ndarray) -> np.ndarray:
    r"""
    Convert an orientation vector to a direction cosine matrix (DCM).

    :param v: :math:`\mathrm{3x1}` or :math:`\mathrm{Tx3x1}` orientation vector, :math:`\mathrm{rad}`
    :type v: np.ndarray

    :return: :math:`\mathrm{3x3}` or :math:`\mathrm{Tx3x3}` direction cosine matrix
    :rtype: np.ndarray
    """
    v = v.flatten()
    alpha = v[np.arange(0, v.size, 3)]
    beta = v[np.arange(1, v.size, 3)]
    gamma = v[np.arange(2, v.size, 3)]

    sin_alpha, cos_alpha = np.sin(alpha), np.cos(alpha)
    sin_beta, cos_beta = np.sin(beta), np.cos(beta)
    sin_gamma, cos_gamma = np.sin(gamma), np.cos(gamma)

    C = np.full((alpha.size, 3, 3), np.nan)
    C[:, 0, 0] = cos_beta * cos_gamma
    C[:, 0, 1] = sin_alpha * sin_beta * cos_gamma - cos_alpha * sin_gamma
    C[:, 0, 2] = sin_alpha * sin_gamma + cos_alpha * sin_beta * cos_gamma
    C[:, 1, 0] = cos_beta * sin_gamma
    C[:, 1, 1] = sin_alpha * sin_beta * sin_gamma + cos_alpha * cos_gamma
    C[:, 1, 2] = -sin_alpha * cos_gamma + cos_alpha * sin_beta * sin_gamma
    C[:, 2, 0] = -sin_beta
    C[:, 2, 1] = sin_alpha * cos_beta
    C[:, 2, 2] = cos_alpha * cos_beta

    return C[0, :, :] if C.shape[0] == 1 else C


def skew_symetric(v: np.ndarray) -> np.ndarray:
    r"""
    Convert a vector to a skew symetric matrix.

    :param v: :math:`\mathrm{3x1}` or :math:`\mathrm{Tx3x1}` vector
    :type v: np.ndarray

    :return: :math:`\mathrm{3x3}` or :math:`\mathrm{Tx3x3}` skew symetric matrix
    :rtype: np.ndarray
    """
    v = v.flatten()
    x = v[np.arange(0, v.size, 3)]
    y = v[np.arange(1, v.size, 3)]
    z = v[np.arange(2, v.size, 3)]

    S = np.zeros((x.size, 3, 3))
    S[:, 0, 1] = -z
    S[:, 0, 2] = y
    S[:, 1, 0] = z
    S[:, 1, 2] = -x
    S[:, 2, 0] = -y
    S[:, 2, 1] = x

    return S[0, :, :] if S.shape[0] == 1 else S
