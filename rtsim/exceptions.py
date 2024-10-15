"""RTSim exceptions."""

from typing import Any  # , Callable


class ComponentTypeError(TypeError):
    """Component type error."""

    def __init__(self, obj: Any, obj_type) -> None:
        """Initialize column count error."""
        super().__init__(f"Expected {obj!r} to be of type {obj_type}.")


class ColCountError(Exception):
    """Column count error."""

    def __init__(self, value: Any, cols: int | None) -> None:
        """Initialize column count error."""
        super().__init__(f"Expected {value!r} to have {cols} columns.")


class FrameTypeError(TypeError):
    """Frame type error."""

    def __init__(self, value: str, frame_type: str) -> None:
        """Initialize frame type error."""
        super().__init__(f"Expected '{value}' to be a {frame_type} coordinate frame.")


class MatrixTypeError(TypeError):
    """Matrix type error."""

    def __init__(self, value: Any) -> None:
        """Initialize matrix type error."""
        super().__init__(f"Expected {value!r} to be a numpy array.")


class MaxValueError(Exception):
    """Maximum value exeeded error."""

    def __init__(self, value: Any, maxvalue: int | float) -> None:
        """Initialize maximum value error."""
        super().__init__(f"Expected {value!r} to be no more than {maxvalue}")


class MinValueError(Exception):
    """Minimum value not met error."""

    def __init__(self, value: Any, minvalue: int | float) -> None:
        """Initialize minimum value error."""
        super().__init__(f"Expected {value!r} to be at least {minvalue}")


class NumDimError(Exception):
    """Number of dimensions error."""

    def __init__(self, value: Any) -> None:
        """Initialize number of dimensions error."""
        super().__init__(f"Expected {value!r} to have 2 or 3 dimensions.")


class NumberTypeError(TypeError):
    """Number type error."""

    def __init__(self, value: Any) -> None:
        """Initialize number type error."""
        super().__init__(f"Expected {value!r} to be an int or float")


class PVATypeError(TypeError):
    """PVA type error."""

    def __init__(self, value: str) -> None:
        """Initialize position, velocity, acceleration type error."""
        super().__init__(f"Expected '{value}' to be ConstantPVA or TimePVA.")


class RowCountError(Exception):
    """Row count error."""

    def __init__(self, value: Any, rows: int | None) -> None:
        """Initialize row count error."""
        super().__init__(f"Expected {value!r} to have {rows} rows.")


class StringError(Exception):
    """String type error."""

    def __init__(self, value: Any) -> None:
        """Initialize string type error."""
        super().__init__(f"Expected {value!r} to be a string.")


class StringLengthError(Exception):
    """String length error."""

    def __init__(self, value: Any) -> None:
        """Initialize string length error."""
        super().__init__(f"Expected {value!r} to be a string of 1 to 140 characters.")


class TimeCountError(Exception):
    """Time step count error."""

    def __init__(self, value: Any) -> None:
        """Initialize time step count error."""
        super().__init__(f"Expected {value!r} to have at least one time step.")
