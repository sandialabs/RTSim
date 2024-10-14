"""Axis component tests."""

import numpy as np
import pytest
from rtsim import Axis
from rtsim import Frame
from rtsim.exceptions import FrameTypeError
from rtsim.pva import ConstantPVA, TimePVA


GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))

CLINEAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TLINEAR = TimePVA(p=GTI, v=GTI, a=GTI)

CANGULAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TANGULAR = TimePVA(p=GTI, v=GTI, a=GTI)


def test_axis_exists():
    """Test if Axis exists."""
    axis = Axis("Generic", Frame(CLINEAR, CANGULAR))
    assert axis


def test_axis_rotating():
    """Test if Axis created with Rotating frame."""
    with pytest.raises(FrameTypeError):
        Axis("Generic", Frame(CLINEAR, TANGULAR))


def test_axis_translocating():
    """Test if Axis created with Translocating frame."""
    with pytest.raises(FrameTypeError):
        Axis("Generic", Frame(TLINEAR, CANGULAR))


def test_axis_full():
    """Test if Axis created with Full frame."""
    with pytest.raises(FrameTypeError):
        Axis("Generic", Frame(TLINEAR, TANGULAR))
