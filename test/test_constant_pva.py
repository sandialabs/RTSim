"""Constant PVA tests."""

import numpy as np
import pytest
from rtsim import ConstantPVA
from rtsim.exceptions import ColCountError, NumDimError, RowCountError

GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))


def test_pva_exists():
    """Verify ConstantPVA class exists."""
    pva = ConstantPVA(p=GCI, v=GCI, a=GCI)
    assert pva


def test_good_pva():
    """Verify ConstantPVA initializes correctly when given correct input."""
    pva = ConstantPVA(p=GCI, v=GCI, a=GCI)
    assert all(pva.p == GCI)
    assert all(pva.v == GCI)
    assert all(pva.a == GCI)


def test_pos_too_few_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        ConstantPVA(p=np.array([1, 2, 3]), v=GCI, a=GCI)


def test_pos_too_many_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        ConstantPVA(p=GTI, v=GCI, a=GCI)


def test_pos_too_few_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        ConstantPVA(p=np.zeros((2, 1)), v=GCI, a=GCI)


def test_pos_too_many_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        ConstantPVA(p=np.zeros((4, 1)), v=GCI, a=GCI)


def test_pos_to_many_columns():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(ColCountError):
        ConstantPVA(p=np.zeros((3, 2)), v=GCI, a=GCI)


def test_vel_too_few_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        ConstantPVA(p=GCI, v=np.array([1, 2, 3]), a=GCI)


def test_vel_too_many_dim():
    """Test the case where a user inputs too many dimensions for the position."""
    with pytest.raises(NumDimError):
        ConstantPVA(p=GCI, v=GTI, a=GCI)


def test_vel_to_few_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        ConstantPVA(p=GCI, v=np.zeros((2, 1)), a=GCI)


def test_vel_to_many_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        ConstantPVA(p=GCI, v=np.zeros((4, 1)), a=GCI)


def test_vel_to_many_columns():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(ColCountError):
        ConstantPVA(p=GCI, v=np.zeros((3, 2)), a=GCI)


def test_accl_too_few_dim():
    """Test the case where a user inputs too few dimensions for the position."""
    with pytest.raises(NumDimError):
        ConstantPVA(p=GCI, v=GCI, a=np.array([1, 2, 3]))


def test_accl_too_many_dim():
    """Test the case where a user inputs too many dimensions for the position."""
    with pytest.raises(NumDimError):
        ConstantPVA(p=GCI, v=GCI, a=GTI)


def test_accl_to_few_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        ConstantPVA(p=GCI, v=GCI, a=np.zeros((2, 1)))


def test_accl_to_many_rows():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(RowCountError):
        ConstantPVA(p=GCI, v=GCI, a=np.zeros((4, 1)))


def test_accl_to_many_columns():
    """Test the case where a user provides too few rows for the position."""
    with pytest.raises(ColCountError):
        ConstantPVA(p=GCI, v=GCI, a=np.zeros((3, 2)))
