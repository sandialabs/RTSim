"""World component tests."""

from math import tau
import numpy as np
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


def test_processing():
    """Test world processing."""
    omega_ie = 72.921151467064e-6
    time = np.arange(0, 100.001, 0.001)
    steps = time.size
    world = World("Terra", 6378137.0, 298.257223563, omega_ie)
    world.process(time)

    assert world.frame.frame_type == "Rotating"
    assert (world.frame.linear.p == 0).all()
    assert (world.frame.linear.v == 0).all()
    assert (world.frame.linear.a == 0).all()
    assert world.frame.angular.p.shape == (steps, 3, 1)
    assert world.frame.angular.v.shape == (steps, 3, 1)
    assert world.frame.angular.a.shape == (steps, 3, 1)

    assert (world.frame.angular.p[-1] == [[0], [0], [omega_ie * 100]]).all()
    assert (world.frame.angular.v[-1] == [[0], [0], [omega_ie]]).all()
    assert (world.frame.angular.a[-1] == 0).all()
