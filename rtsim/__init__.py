"""
The ``RTSim`` package.

RTSim is a Python module for simulating the inertial outputs of rotational testbeds (RT).
"""

from .body import Body
from .frame import Frame
from .mount import Mount
from .pva import ConstantPVA, TimePVA

__version__ = "0.0.1"
