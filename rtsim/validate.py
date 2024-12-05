"""
RTSim validators.

Copyright © 2024, National Technology & Engineering Solutions of
Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with
NTESS, the U.S. Government retains certain rights in this software.
"""

# SPDX-License-Identifier: BSD-3-Clause

import numpy as np
from .exceptions import (
    ComponentTypeError,
    ColCountError,
    MatrixTypeError,
    MaxValueError,
    MinValueError,
    NumDimError,
    NumberTypeError,
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


def number(value, minvalue=None, maxvalue=None):
    """Validate number input."""
    if not isinstance(value, (int, float)):
        raise NumberTypeError(value)
    if minvalue is not None and value < minvalue:
        raise MinValueError(value, minvalue)
    if maxvalue is not None and value > maxvalue:
        raise MaxValueError(value, maxvalue)


def component(obj, obj_type):
    """Validate component type."""
    if not isinstance(obj, obj_type):
        raise ComponentTypeError(obj, obj_type)


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
