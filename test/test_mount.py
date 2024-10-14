"""Mount component tests."""

import numpy as np
import pytest
from rtsim import Mount
from rtsim import Frame
from rtsim.exceptions import FrameTypeError
from rtsim.pva import ConstantPVA, TimePVA


GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))

CLINEAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TLINEAR = TimePVA(p=GTI, v=GTI, a=GTI)

CANGULAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TANGULAR = TimePVA(p=GTI, v=GTI, a=GTI)


def test_mount_exists():
    """Test if Mount exists."""
    mount = Mount("Generic", Frame(CLINEAR, CANGULAR))
    assert mount


def test_mount_rotating():
    """Test Mount created with Rotating frame."""
    with pytest.raises(FrameTypeError):
        Mount("Generic", Frame(CLINEAR, TANGULAR))


def test_mount_translocating():
    """Test Mount created with Translocating frame."""
    with pytest.raises(FrameTypeError):
        Mount("Generic", Frame(TLINEAR, CANGULAR))


def test_mount_full():
    """Test Mount created with Full frame."""
    with pytest.raises(FrameTypeError):
        Mount("Generic", Frame(TLINEAR, TANGULAR))
