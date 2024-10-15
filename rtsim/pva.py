"""Position, Velocity, and Acceleration classes."""

import numpy as np
from rtsim import validate


class ConstantPVA:
    """Constant Position, Velocity, Acceleration class."""

    def __init__(self, *, p: np.ndarray, v: np.ndarray, a: np.ndarray) -> None:
        """
        Initialize a constant PVA.

        :param p: Position (3x1)
        :type p: np.ndarray

        :param v: Velocity (3x1)
        :type v: np.ndarray

        :param a: Acceleration (3x1)
        :type a: np.ndarray
        """
        self.p = p
        self.v = v
        self.a = a

    @property
    def p(self):
        """Position vector."""
        return self._p

    @p.setter
    def p(self, value):
        validate.constant_vector(value)
        self._p = value

    @property
    def v(self):
        """Velocity vector."""
        return self._v

    @v.setter
    def v(self, value):
        validate.constant_vector(value)
        self._v = value

    @property
    def a(self):
        """Acceleration vector."""
        return self._a

    @a.setter
    def a(self, value):
        validate.constant_vector(value)
        self._a = value

    def __repr__(self) -> str:
        """Return a string representation of the constant PVA."""
        return f"ConstantPVA(\n p={self.p!r},\n v={self.v!r},\n a={self.a!r}\n)"

    def __str__(self) -> str:
        """Return a string representation of the constant PVA."""
        return "\n".join(
            [
                "ConstantPVA(",
                f"  p = {'x'.join([str(x) for x in self.p.shape])} Array,",
                f"  v = {'x'.join([str(x) for x in self.v.shape])} Array,",
                f"  a = {'x'.join([str(x) for x in self.a.shape])} Array,",
                ")",
            ]
        )


class TimePVA:
    """Time varying Position, Velocity, Acceleration class."""

    def __init__(self, *, p: np.ndarray, v: np.ndarray, a: np.ndarray) -> None:
        """
        Initialize a time varying PVA.

        :param p: Position (Tx3x1)
        :type p: np.ndarray

        :param v: Velocity (Tx3x1)
        :type v: np.ndarray

        :param a: Acceleration (Tx3x1)
        :type a: np.ndarray
        """
        self.p = p
        self.v = v
        self.a = a

    @property
    def p(self):
        """Position vector."""
        return self._p

    @p.setter
    def p(self, value):
        validate.time_vector(value)
        self._p = value

    @property
    def v(self):
        """Velocity vector."""
        return self._v

    @v.setter
    def v(self, value):
        validate.time_vector(value)
        self._v = value

    @property
    def a(self):
        """Acceleration vector."""
        return self._a

    @a.setter
    def a(self, value):
        validate.time_vector(value)
        self._a = value

    def __repr__(self) -> str:
        """Return a string representation of the time varying PVA."""
        return f"TimePVA(\n p={self.p!r},\n v={self.v!r},\n a={self.a!r}\n)"

    def __str__(self) -> str:
        """Return a string representation of the time varying PVA."""
        return "\n".join(
            [
                "TimePVA(",
                f"  p = {'x'.join([str(x) for x in self.p.shape])} Array,",
                f"  v = {'x'.join([str(x) for x in self.v.shape])} Array,",
                f"  a = {'x'.join([str(x) for x in self.a.shape])} Array,",
                ")",
            ]
        )
