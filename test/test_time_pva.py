"""Constant PVA tests."""

import numpy as np
import pytest
from rtsim import TimePVA
from rtsim.exceptions import ColCountError, NumDimError, RowCountError

GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))


def test_pva_exists():
    """Verify TimePVA class exists."""
    pva = TimePVA(p=GTI, v=GTI, a=GTI)
    assert pva


def test_good_pva():
    """Verify TimePVA initializes correctly when given correct input."""
    pva = TimePVA(p=GTI, v=GTI, a=GTI)
    assert (pva.p == GTI).all()
    assert (pva.v == GTI).all()
    assert (pva.a == GTI).all()


def test_pos_too_few_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        TimePVA(p=GCI, v=GTI, a=GTI)


def test_pos_too_many_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        TimePVA(p=np.zeros((5, 5, 3, 1)), v=GTI, a=GTI)


def test_pos_too_few_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        TimePVA(p=np.zeros((5, 2, 1)), v=GTI, a=GTI)


def test_pos_too_many_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        TimePVA(p=np.zeros((5, 4, 1)), v=GTI, a=GTI)


def test_pos_to_many_columns():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(ColCountError):
        TimePVA(p=np.zeros((5, 3, 2)), v=GTI, a=GTI)


def test_vel_too_few_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        TimePVA(p=GTI, v=GCI, a=GTI)


def test_vel_too_many_dim():
    """Test the case where a user inputs too many dimensions for the position."""
    with pytest.raises(NumDimError):
        TimePVA(p=GTI, v=np.zeros((5, 5, 3, 1)), a=GTI)


def test_vel_to_few_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        TimePVA(p=GTI, v=np.zeros((5, 2, 1)), a=GTI)


def test_vel_to_many_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        TimePVA(p=GTI, v=np.zeros((5, 4, 1)), a=GTI)


def test_vel_to_many_columns():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(ColCountError):
        TimePVA(p=GTI, v=np.zeros((5, 3, 2)), a=GTI)


def test_accl_too_few_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        TimePVA(p=GTI, v=GTI, a=GCI)


def test_accl_too_many_dim():
    """Test the case where a user inputs too many dimensions for the position."""
    with pytest.raises(NumDimError):
        TimePVA(p=GTI, v=GTI, a=np.zeros((5, 5, 3, 1)))


def test_accl_to_few_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        TimePVA(p=GTI, v=GTI, a=np.zeros((5, 2, 1)))


def test_accl_to_many_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        TimePVA(p=GTI, v=GTI, a=np.zeros((5, 4, 1)))


def test_accl_to_many_columns():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(ColCountError):
        TimePVA(p=GTI, v=GTI, a=np.zeros((5, 3, 2)))
