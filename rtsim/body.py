"""Body (system under test) component."""

from .base import Base
from .exceptions import FrameTypeError
from .frame import Frame


class Body(Base):
    """Representation of a system under test (body)."""

    def __init__(self, moniker: str, frame: Frame) -> None:
        """
        Initialize body (system under test).

        :param moniker: Name of the body.
        :type moniker: str

        :param frame: Coordinate frame of the body.
        :type frame: Frame[Fixed]

        :raises FrameTypeError: If the body coordinate frame type is not 'Fixed'.
        """
        super().__init__(moniker)

        if frame.frame_type != "Fixed":
            var_name = "frame"
            raise FrameTypeError(var_name, "Fixed")

        self.frame = frame
