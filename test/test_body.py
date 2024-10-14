"""Body component tests."""

import numpy as np
import pytest
from rtsim import Body
from rtsim import Frame
from rtsim.exceptions import FrameTypeError
from rtsim.pva import ConstantPVA, TimePVA


GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))

CLINEAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TLINEAR = TimePVA(p=GTI, v=GTI, a=GTI)

CANGULAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TANGULAR = TimePVA(p=GTI, v=GTI, a=GTI)


def test_body_exists():
    """Test if Body exists."""
    body = Body("Generic", Frame(CLINEAR, CANGULAR))
    assert body


def test_body_rotating():
    """Test if Body created with Rotating frame."""
    with pytest.raises(FrameTypeError):
        Body("Generic", Frame(CLINEAR, TANGULAR))


def test_body_translocating():
    """Test if Body created with Translocating frame."""
    with pytest.raises(FrameTypeError):
        Body("Generic", Frame(TLINEAR, CANGULAR))


def test_body_full():
    """Test if Body created with Full frame."""
    with pytest.raises(FrameTypeError):
        Body("Generic", Frame(TLINEAR, TANGULAR))
