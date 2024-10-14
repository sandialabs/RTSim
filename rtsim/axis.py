"""Axis component."""

from .base import Base
from .exceptions import FrameTypeError
from .frame import Frame


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
