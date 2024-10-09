"""Position, Velocity, and Acceleration vector tests."""

import rtsim


def test_constant_pva_exists():
    """Verify ConstantPVA class exists."""
    cpva = rtsim.ConstantPVA()
    assert cpva


def test_time_pva_exists():
    """Verify TimePVA class exists."""
    tpva = rtsim.TimePVA()
    assert tpva
