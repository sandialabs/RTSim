"""RTSim validators."""

import numpy as np
from .exceptions import (
    ColCountError,
    MatrixTypeError,
    NumDimError,
    RowCountError,
    StringError,
    StringLengthError,
    TimeCountError,
)

CONSTANT_NDIM = 2
TIME_NDIM = 3
ROWS = 3
COLS = 1


def constant_vector(value):
    """Validate constant vector."""
    if not isinstance(value, np.ndarray):
        raise MatrixTypeError(value)

    if value.ndim != CONSTANT_NDIM:
        raise NumDimError(value)

    shape = value.shape

    if shape[0] != ROWS:
        raise RowCountError(value, ROWS)

    if shape[1] != COLS:
        raise ColCountError(value, COLS)


def string(value):
    """Validate string input."""
    if not isinstance(value, str):
        raise StringError(value)
    too_long = 141
    if not (0 < len(value) < too_long):
        raise StringLengthError(value)


def time_vector(value):
    """Validate time vector."""
    if not isinstance(value, np.ndarray):
        raise MatrixTypeError(value)

    if value.ndim != TIME_NDIM:
        raise NumDimError(value)

    shape = value.shape

    if shape[0] < 1:
        raise TimeCountError(value)

    if shape[1] != ROWS:
        raise RowCountError(value, ROWS)

    if shape[2] != COLS:
        raise ColCountError(value, COLS)
