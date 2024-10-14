"""Frame tests."""

import numpy as np
from rtsim.frame import Frame
from rtsim.pva import ConstantPVA, TimePVA

GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))

CLINEAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TLINEAR = TimePVA(p=GTI, v=GTI, a=GTI)

CANGULAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TANGULAR = TimePVA(p=GTI, v=GTI, a=GTI)


def test_frame_exists():
    """Verify ConstantPVA class exists."""
    frame = Frame(linear=CLINEAR, angular=CANGULAR)
    assert frame


def test_fixed_frame():
    """Verify creation of Fixed coordinate frame."""
    frame = Frame(linear=CLINEAR, angular=CANGULAR)
    assert frame.frame_type == "Fixed"
    ndim = 2
    assert frame.C.ndim == ndim
    assert frame.Omega.ndim == ndim
    assert frame.Omega_dot.ndim == ndim


def test_rotating_frame():
    """Verify creation of Rotating coordinate frame."""
    frame = Frame(linear=CLINEAR, angular=TANGULAR)
    assert frame.frame_type == "Rotating"
    ndim = 3
    assert frame.C.ndim == ndim
    assert frame.Omega.ndim == ndim
    assert frame.Omega_dot.ndim == ndim


def test_translocating_frame():
    """Verify creation of Translocating coordinate frame."""
    frame = Frame(linear=TLINEAR, angular=CANGULAR)
    assert frame.frame_type == "Translocating"
    ndim = 2
    assert frame.C.ndim == ndim
    assert frame.Omega.ndim == ndim
    assert frame.Omega_dot.ndim == ndim


def test_full_frame():
    """Verify creation of Full coordinate frame."""
    frame = Frame(linear=TLINEAR, angular=TANGULAR)
    assert frame.frame_type == "Full"
    ndim = 3
    assert frame.C.ndim == ndim
    assert frame.Omega.ndim == ndim
    assert frame.Omega_dot.ndim == ndim
