"""Axis component tests."""

from math import tau
import numpy as np
import pytest
from rtsim import Axis, Body, Mount
from rtsim import Frame
from rtsim.exceptions import FrameTypeError
from rtsim.pva import ConstantPVA, TimePVA


GCI = np.zeros((3, 1))
GTI = np.zeros((5, 3, 1))

CLINEAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TLINEAR = TimePVA(p=GTI, v=GTI, a=GTI)

CANGULAR = ConstantPVA(p=GCI, v=GCI, a=GCI)
TANGULAR = TimePVA(p=GTI, v=GTI, a=GTI)

MU = Frame(
    linear=TimePVA(p=np.zeros((500, 3, 1)), v=np.zeros((500, 3, 1)), a=np.zeros((500, 3, 1))),
    angular=TimePVA(p=np.zeros((500, 3, 1)), v=np.zeros((500, 3, 1)), a=np.zeros((500, 3, 1))),
)

RHO = Frame(
    linear=ConstantPVA(p=np.zeros((3, 1)), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
    angular=TimePVA(p=np.zeros((500, 3, 1)), v=np.zeros((500, 3, 1)), a=np.zeros((500, 3, 1))),
)

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

ALPHA = ConstantPVA(
    p=MOUNT.frame.linear.p + MOUNT.frame.C @ BODY.frame.linear.p,
    v=np.zeros((3, 1)),
    a=np.zeros((3, 1)),
)

OMEGA = ConstantPVA(p=np.zeros((3, 1)), v=np.zeros((3, 1)), a=np.zeros((3, 1)))


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


def test_process():
    """Test axis processing."""
    axis = Axis(
        "SART Axis",
        Frame(
            linear=ConstantPVA(p=np.array([[0.0], [0.0], [-0.0762]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
            angular=ConstantPVA(p=np.array([[0.0], [tau / 2], [0.0]]), v=np.zeros((3, 1)), a=np.zeros((3, 1))),
        ),
    )

    new_alpha, new_omega = axis.process(MU, RHO, ALPHA, OMEGA)

    assert isinstance(new_alpha, TimePVA)
    assert isinstance(new_omega, TimePVA)
    assert (new_alpha.p == 0).all()
    assert (new_alpha.v == 0).all()
    assert (new_alpha.a == 0).all()
    assert (new_omega.p == 0).all()
    assert (new_omega.v == 0).all()
    assert (new_omega.a == 0).all()
