"""Mount component."""

from .base import Base
from .exceptions import FrameTypeError
from .frame import Frame


class Mount(Base):
    """Representation of a system under test's mount."""

    def __init__(self, moniker: str, frame: Frame) -> None:
        """
        Initialize mount.

        :param moniker: Name of the mount.
        :type moniker: str

        :param frame: Coordinate frame of the mount.
        :type frame: Frame[Fixed]

        :raises FrameTypeError: If the mount coordinate frame type is not 'Fixed'.
        """
        super().__init__(moniker)

        if frame.frame_type != "Fixed":
            var_name = "frame"
            raise FrameTypeError(var_name, "Fixed")

        self.frame = frame
