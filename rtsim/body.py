"""
RTSim Body (system under test) component.

Copyright © 2024, National Technology & Engineering Solutions of
Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with
NTESS, the U.S. Government retains certain rights in this software.
"""

# SPDX-License-Identifier: BSD-3-Clause

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
