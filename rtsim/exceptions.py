"""RTSim exceptions."""

from typing import Any  # , Callable


class ColCountError(Exception):
    """Column count error."""

    def __init__(self, value: Any, cols: int | None) -> None:
        """Initialize column count error."""
        super().__init__(f"Expected {value!r} to have {cols} columns.")


class MatrixTypeError(TypeError):
    """Matrix type error."""

    def __init__(self, value: Any) -> None:
        """Initialize matrix type error."""
        super().__init__(f"Expected {value!r} to be a numpy array.")


class NumDimError(Exception):
    """Number of dimensions error."""

    def __init__(self, value: Any) -> None:
        """Initialize number of dimensions error."""
        super().__init__(f"Expected {value!r} to have 2 or 3 dimensions.")


class RowCountError(Exception):
    """Row count error."""

    def __init__(self, value: Any, rows: int | None) -> None:
        """Initialize row count error."""
        super().__init__(f"Expected {value!r} to have {rows} rows.")


class TimeCountError(Exception):
    """Time step count error."""

    def __init__(self, value: Any) -> None:
        """Initialize time step count error."""
        super().__init__(f"Expected {value!r} to have at least one time step.")
