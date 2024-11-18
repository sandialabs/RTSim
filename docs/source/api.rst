***
API
***

.. module:: rtsim

Core
====

.. autoclass:: Axis
    :members:

.. autoclass:: Body
    :members:

.. autoclass:: Mount
    :members:

.. autoclass:: Testbed
    :members:

.. autoclass:: World
    :members:

Frames
======
Frames are used by the `core` classes to instantiate the relevant coordinate frames.

.. autoclass:: Fixed

.. autoclass:: Full

.. autoclass:: Rotating

.. autoclass:: Translocating

.. autofunction:: rtsim.frames.orientation_to_dcm

.. autofunction:: rtsim.frames.skew_symetric

Descriptors
===========
Descriptors are used by the `core` and `frame` classes to validate valiables.

.. autoclass:: rtsim.descriptors.Moniker

.. autoclass:: rtsim.descriptors.Constant

.. autoclass:: rtsim.descriptors.Constant_Vector

.. autoclass:: rtsim.descriptors.Time_Vector

.. autoclass:: rtsim.descriptors.Constant_Matrix

.. autoclass:: rtsim.descriptors.Time_Matrix
