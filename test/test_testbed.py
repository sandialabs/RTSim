"""Testbed tests."""

from math import tau
import numpy as np
import pytest
from rtsim import Axis, Body, Frame, Mount, Testbed, World, ConstantPVA
from rtsim.exceptions import ComponentTypeError, MaxValueError, MinValueError, NumberTypeError


BODY = Body(
    "Generic",
    Frame(
        linear=ConstantPVA(p=np.array([[0.0], [0.0], [0.0508]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
        angular=ConstantPVA(p=np.array([[0.0], [tau / 2], [0.0]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
    ),
)

MOUNT = Mount(
    "Generic",
    Frame(
        linear=ConstantPVA(p=np.array([[0.0], [0.0], [0.0254]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
        angular=ConstantPVA(p=np.zeros((3, 1)), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
    ),
)

AXIS = Axis(
    "SART Axis",
    Frame(
        linear=ConstantPVA(p=np.array([[0.0], [0.0], [-0.0762]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
        angular=ConstantPVA(p=np.array([[0.0], [tau / 2], [0.0]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
    ),
)

WORLD = World("Terra", 6378137.0, 298.257223563, 72.921151467064e-6)


def test_testbed_exists():
    """Test existence of Testbed class."""
    testbed = Testbed(
        "SART", llhg=(35.05133916, -106.54504361, 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY)
    )
    assert testbed


def test_lat_not_number():
    """Test latitude not a number."""
    with pytest.raises(NumberTypeError):
        Testbed("SART", llhg=("35.051", -106.54504361, 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_lat_neg_range():
    """Test latitude < -90 deg."""
    with pytest.raises(MinValueError):
        Testbed("SART", llhg=(-90.1, -106.54504361, 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_lat_pos_range():
    """Test latitude > 180 deg."""
    with pytest.raises(MaxValueError):
        Testbed("SART", llhg=(90.1, -106.54504361, 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_lon_not_number():
    """Test longitude not a number."""
    with pytest.raises(NumberTypeError):
        Testbed("SART", llhg=(35.05133916, "-106.545", 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_lon_neg_range():
    """Test latitude < -180 deg."""
    with pytest.raises(MinValueError):
        Testbed("SART", llhg=(35.05133916, -180.1, 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_lon_pos_range():
    """Test latitude > 180 deg."""
    with pytest.raises(MaxValueError):
        Testbed("SART", llhg=(35.05133916, 180.1, 1625.57, 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_hae_not_number():
    """Test HAE not a number."""
    with pytest.raises(NumberTypeError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, "162", 9.7920631997), components=(WORLD, [AXIS], MOUNT, BODY))


def test_grav_not_number():
    """Test gravity not a number."""
    with pytest.raises(NumberTypeError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, 1625.57, "9.792063"), components=(WORLD, [AXIS], MOUNT, BODY))


def test_grav_neg_range():
    """Test latitude < 0 m/s."""
    with pytest.raises(MinValueError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, 1625.57, -9.7920631), components=(WORLD, [AXIS], MOUNT, BODY))


def test_world_incorrect():
    """Test world of inccorrect type."""
    with pytest.raises(ComponentTypeError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, 1625.57, 9.7920631), components=(MOUNT, [AXIS], MOUNT, BODY))


def test_axis_incorrect():
    """Test axis of inccorrect type."""
    with pytest.raises(ComponentTypeError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, 1625.6, 9.7920631), components=(WORLD, [WORLD], MOUNT, BODY))


def test_single_axis_incorrect():
    """Test one axis of inccorrect type."""
    with pytest.raises(ComponentTypeError):
        Testbed(
            "SART", llhg=(35.05133916, -106.54504361, 1625.6, 9.792063), components=(WORLD, [AXIS, WORLD], MOUNT, BODY)
        )


def test_mount_incorrect():
    """Test mount of inccorrect type."""
    with pytest.raises(ComponentTypeError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, 1625.57, 9.7920631), components=(WORLD, [AXIS], WORLD, BODY))


def test_body_incorrect():
    """Test body of inccorrect type."""
    with pytest.raises(ComponentTypeError):
        Testbed("SART", llhg=(35.05133916, -106.54504361, 1625.57, 9.792063), components=(WORLD, [AXIS], MOUNT, WORLD))
