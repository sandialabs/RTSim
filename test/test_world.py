"""World component tests."""

from math import tau
import pytest
from rtsim import World
from rtsim.exceptions import MaxValueError, MinValueError, NumberTypeError


def test_world_exists():
    """Test if World exists."""
    world = World("Terra", 6378137.0, 298.257223563, 72.921151467064e-6)
    assert world


def test_non_number_sma():
    """Test if semi-major-axis is not a number."""
    with pytest.raises(NumberTypeError):
        World("Terra", "6378137.0", 298.257223563, 72.921151467064e-6)


def test_neg_sma():
    """Test if semi-major-axis is negative."""
    with pytest.raises(MinValueError):
        World("Terra", -1.0, 298.257223563, 72.921151467064e-6)


def test_non_number_iflat():
    """Test if inverse flattening is not a number."""
    with pytest.raises(TypeError):
        World("Terra", 6378137.0, "298.257223563", 72.921151467064e-6)


def test_non_number_rot_rate():
    """Test if rotation rate is not a number."""
    with pytest.raises(NumberTypeError):
        World("Terra", 6378137.0, 298.257223563, "72.921151467064e-6")


def test_neg_rot_rate():
    """Test if rotation rate is negative."""
    with pytest.raises(MinValueError):
        World("Terra", 6378137.0, 298.257223563, -0.00001)


def test_large_rot_rate():
    """Test if rotation rate is too large."""
    with pytest.raises(MaxValueError):
        World("Terra", 6378137.0, 298.257223563, tau + 0.00001)
