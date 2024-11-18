***********
Mathematics
***********
A rotational testbed may be comprised of any number of rotating axes. We will designate the total number of axes as :math:`A` and an individual axis as :math:`a` where :math:`a = 1 \dots A`. The most typical rotational testbed include:

    - A basic centrifuge, or a single axis rate table :math:`\rightarrow A = 1`
    - A centrifuge with a counter-rotating platform, or a two axis rate table :math:`\rightarrow A = 2`
    - A centrifuge with a two-axis platform, or a three axis rate table :math:`\rightarrow A = 3`

The axis designated as :math:`a=1` is the axis to which a system under test (SUT) is rigidly attached. Axes are then number outwardly such that a rotation of the axis moves all lower axes. For example, axis :math:`a=2` only moves axis :math:`a=1` and axis :math:`a=3` moves both axes :math:`a=2` and :math:`a=1`.

Angular Rate
============
For a single axis testbed :math:`(A=1)`, the rate of rotation of the body :math:`(\mathrm{b})` frame relative to the inertial :math:`(\mathrm{i})` frame resolved in the inertial frame is the sum of the rates of rotation of all the intermediate frames.

.. math::
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) = \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t) + \boldsymbol{\omega}^\mathrm{i}_{\mathrm{e}\mathrm{n}}(t) + \boldsymbol{\omega}^\mathrm{i}_{\mathrm{n}{\zeta_1}}(t) + \boldsymbol{\omega}^\mathrm{i}_{{\zeta_1}{\mu_1}}(t) + \boldsymbol{\omega}^\mathrm{i}_{{\mu_1}{\rho_1}}(t) + \boldsymbol{\omega}^\mathrm{i}_{{\rho_1}\mathrm{m}}(t) + \boldsymbol{\omega}^\mathrm{i}_{\mathrm{m}\mathrm{b}}(t)

.. note::
    A detailed discussion of the pertinent coordinate frames and their relational parameters may be found in `Coordinate Frames <frames.html#Coordinate Frames>`_.

All of the right hand terms other than :math:`\boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)` are difficult to measure in the inertial frame. Therefore, we convert them to the frames in which each parameter may be easily measured to get:

.. math::
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
    &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{\omega}^\mathrm{e}_{\mathrm{e}\mathrm{n}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \mathbf{C}^\mathrm{e}_\mathrm{n}\; \boldsymbol{\omega}^\mathrm{n}_{\mathrm{n}{\zeta_1}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \mathbf{C}^\mathrm{e}_\mathrm{n}\; \mathbf{C}^\mathrm{n}_{\zeta_1}\; \boldsymbol{\omega}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \mathbf{C}^\mathrm{e}_\mathrm{n}\; \mathbf{C}^\mathrm{n}_{\zeta_1}\; \mathbf{C}^{\zeta_1}_{\mu_1}(t)\; \boldsymbol{\omega}^{\mu_1}_{{\mu_1}{\rho_1}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \mathbf{C}^\mathrm{e}_\mathrm{n}\; \mathbf{C}^\mathrm{n}_{\zeta_1}\; \mathbf{C}^{\zeta_1}_{\mu_1}(t)\; \mathbf{C}^{\mu_1}_{\rho_1}\; \boldsymbol{\omega}^{\rho_1}_{{\rho_1}\mathrm{m}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \mathbf{C}^\mathrm{e}_\mathrm{n}\; \mathbf{C}^\mathrm{n}_{\zeta_1}\; \mathbf{C}^{\zeta_1}_{\mu_1}(t)\; \mathbf{C}^{\mu_1}_{\rho_1}\; \mathbf{C}^{\rho_1}_\mathrm{m} \; \boldsymbol{\omega}^\mathrm{m}_{\mathrm{m}\mathrm{b}}(t)

Using the relational parameters discussed in `Coordinate Frames <frames.html#Coordinate Frames>`_, the angular rate reduces to:

.. math::
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
    &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_1}\;
    \boldsymbol{\omega}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_1}\;
    \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
    \boldsymbol{\omega}^{\mu_1}_{{\mu_1}{\rho_1}}(t)

Performing the same procedure for a two axis testbed :math:`(A=2)` and a three axis testbed :math:`(A=3)` resolves to:

.. math::
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
    &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_2}\;
    \boldsymbol{\omega}^{\zeta_2}_{{\zeta_2}{\mu_2}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_2}\;
    \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
    \boldsymbol{\omega}^{\mu_2}_{{\mu_2}{\rho_2}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_2}\;
    \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
    \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
    \mathbf{C}^{\rho_2}_{\zeta_1}\;
    \boldsymbol{\omega}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_2}\;
    \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
    \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
    \mathbf{C}^{\rho_2}_{\zeta_1}\;
    \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
    \boldsymbol{\omega}^{\mu_1}_{{\mu_1}{\rho_1}}(t)

and

.. math::
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
    &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_3}\;
    \boldsymbol{\omega}^{\zeta_3}_{{\zeta_3}{\mu_3}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_3}\;
    \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
    \boldsymbol{\omega}^{\mu_3}_{{\mu_3}{\rho_3}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_3}\;
    \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
    \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
    \mathbf{C}^{\rho_3}_{\zeta_2}\;
    \boldsymbol{\omega}^{\zeta_2}_{{\zeta_2}{\mu_2}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_3}\;
    \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
    \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
    \mathbf{C}^{\rho_3}_{\zeta_2}\;
    \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
    \boldsymbol{\omega}^{\mu_2}_{{\mu_2}{\rho_2}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_3}\;
    \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
    \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
    \mathbf{C}^{\rho_3}_{\zeta_2}\;
    \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
    \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
    \mathbf{C}^{\rho_2}_{\zeta_1}\;
    \boldsymbol{\omega}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
    &+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
    \mathbf{C}^\mathrm{e}_\mathrm{n}\;
    \mathbf{C}^\mathrm{n}_{\zeta_3}\;
    \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
    \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
    \mathbf{C}^{\rho_3}_{\zeta_2}\;
    \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
    \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
    \mathbf{C}^{\rho_2}_{\zeta_1}\;
    \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
    \boldsymbol{\omega}^{\mu_1}_{{\mu_1}{\rho_1}}(t)

This progression continues for any positive number of testbed axes. However, these three equations are enough to notice a pattern. As a result, we may define the following variables:

.. math::
    \boldsymbol{\omega}_0(t) &= 0\\[1em]
    \boldsymbol{\omega}_1(t) &= \mathbf{C}^\mathrm{h}_{\zeta_1}\; \left[\boldsymbol{\omega}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t) + \mathbf{C}^{\zeta_1}_{\mu_1}(t)\; \boldsymbol{\omega}^{\mu_1}_{{\mu_1}{\rho_1}}(t) + \mathbf{C}^{\zeta_1}_{\mu_1}(t)\; \mathbf{C}^{\mu_1}_{\rho_1}(t)\; \boldsymbol{\omega}_0(t)\right]\\[1em]
    \boldsymbol{\omega}_2(t) &= \mathbf{C}^\mathrm{h}_{\zeta_2}\; \left[\boldsymbol{\omega}^{\zeta_2}_{{\zeta_2}{\mu_2}}(t) + \mathbf{C}^{\zeta_2}_{\mu_2}(t)\; \boldsymbol{\omega}^{\mu_2}_{{\mu_2}{\rho_2}}(t) + \mathbf{C}^{\zeta_2}_{\mu_2}(t)\; \mathbf{C}^{\mu_2}_{\rho_2}(t)\; \boldsymbol{\omega}_1(t)\right]\\[1em]
    \boldsymbol{\omega}_3(t) &= \mathbf{C}^\mathrm{h}_{\zeta_3}\; \left[\boldsymbol{\omega}^{\zeta_3}_{{\zeta_3}{\mu_3}}(t) + \mathbf{C}^{\zeta_3}_{\mu_3}(t)\; \boldsymbol{\omega}^{\mu_3}_{{\mu_3}{\rho_3}}(t) + \mathbf{C}^{\zeta_3}_{\mu_3}(t)\; \mathbf{C}^{\mu_3}_{\rho_3}(t)\; \boldsymbol{\omega}_2(t)\right]

Using these definitions, the three angular rate equations simplify to:

.. math::
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\omega}_1(t)\\[1em]
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\omega}_2(t)\\[1em]
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\omega}_3(t)

Now, using the definitions and final angular rate equation forms we may define modular equations for the angular rate of a general testbed :math:`(A>0)` as:

.. math::
    \boldsymbol{\omega}_0(t) &= 0\\[1em]
    \boldsymbol{\omega}_a(t) &= \mathbf{C}^\mathrm{h}_{\zeta_a}\; \left[\boldsymbol{\omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \boldsymbol{\omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t) + \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\; \boldsymbol{\omega}_{a-1}(t)\right]\\[1em]
    \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) &= \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\omega}_A(t)

Angular Acceleration
====================
The angular acceleration of a general testbed is produced by applying the sum and product rules to the angular rate equations to provide:

.. math::
    \begin{align}
        \dot{\boldsymbol{\omega}}_0(t) &= 0\\[1em]
        \dot{\boldsymbol{\omega}}_a(t)
        &= \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \dot{\boldsymbol{\omega}}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\\
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \dot{\mathbf{C}}^{\zeta_a}_{\mu_a}(t)\; \boldsymbol{\omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\\
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \dot{\boldsymbol{\omega}}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\\
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \dot{\mathbf{C}}^{\zeta_a}_{\mu_a}(t)\;
        \mathbf{C}^{\mu_a}_{\rho_a}(t)\;
        \boldsymbol{\omega}_{a-1}(t)\\
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \dot{\mathbf{C}}^{\mu_a}_{\rho_a}(t)\;
        \boldsymbol{\omega}_{a-1}(t)\\
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \mathbf{C}^{\mu_a}_{\rho_a}(t)\;
        \dot{\boldsymbol{\omega}}_{a-1}(t)\\[1em]
        \dot{\boldsymbol{\omega}}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
        &= \dot{\mathbf{C}}^\mathrm{i}_\mathrm{n}(t)\;
        \boldsymbol{\omega}_A(t)
        + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\;
        \dot{\boldsymbol{\omega}}_A(t)
    \end{align}

Applying the first derivative of the DCMs (see `DCM Derivatives <frames.html#derivatives>`_) to remove the need for calculating the derivatives numerically, produces the angular acceleration equations:

.. math::
    \begin{align}
        \dot{\boldsymbol{\omega}}_0(t) &= 0\\[1em]
        \dot{\boldsymbol{\omega}}_a(t)
        &= \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \dot{\boldsymbol{\omega}}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\\\notag
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \boldsymbol{\Omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \boldsymbol{\omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\\\notag
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \dot{\boldsymbol{\omega}}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\\\notag
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \boldsymbol{\Omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \mathbf{C}^{\mu_a}_{\rho_a}(t)\;
        \boldsymbol{\omega}_{a-1}(t)\\\notag
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \boldsymbol{\Omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\;
        \boldsymbol{\omega}_{a-1}(t)\\\notag
        &+ \mathbf{C}^\mathrm{h}_{\zeta_a}\;
        \mathbf{C}^{\zeta_a}_{\mu_a}(t)\;
        \mathbf{C}^{\mu_a}_{\rho_a}(t)\;
        \dot{\boldsymbol{\omega}}_{a-1}(t)\\[1em]
        \dot{\boldsymbol{\omega}}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
        &= \boldsymbol{\Omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\;
        \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\;
        \boldsymbol{\omega}_A(t) + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \dot{\boldsymbol{\omega}}_A(t)
    \end{align}

Linear Position
===============
As with the angular rate, the linear position of the :math:`\mathrm{b}` frame relative to the :math:`\mathrm{i}` frame resolved in the :math:`\mathrm{i}` frame for a single axis testbed :math:`(A=1)` is the sum of the positions of all the intermediate frames.

.. math::
	\boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
	= \boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)
	+ \boldsymbol{r}^\mathrm{i}_{\mathrm{e}\mathrm{n}}(t)
	+ \boldsymbol{r}^\mathrm{i}_{\mathrm{n}{\zeta_1}}(t)
	+ \boldsymbol{r}^\mathrm{i}_{{\zeta_1}{\mu_1}}(t)
	+ \boldsymbol{r}^\mathrm{i}_{{\mu_1}{\rho_1}}(t)
	+ \boldsymbol{r}^\mathrm{i}_{{\rho_1}\mathrm{m}}(t)
	+ \boldsymbol{r}^\mathrm{i}_{\mathrm{m}\mathrm{b}}(t)

All of the right hand terms except :math:`\boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)` are difficult to measure in the :math:`\mathrm{i}` frame. Therefore, we convert them to frames in which the parameters may be easily measured:

.. math::
	\boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
	&= \boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \boldsymbol{r}^\mathrm{n}_{\mathrm{n}{\zeta_1}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \boldsymbol{r}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
       \boldsymbol{r}^{\mu_1}_{{\mu_1}{\rho_1}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
       \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
       \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \mathbf{C}^{\rho_1}_\mathrm{m}\;
       \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}(t)

Using the relational parameters discussed in `Coordinate Frames <frames.html#Coordinate Frames>`_, the linear position reduces to:

.. math::
	\boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)
	&= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \boldsymbol{r}^\mathrm{n}_{\mathrm{n}{\zeta_1}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \boldsymbol{r}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
       \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_1}\;
       \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
       \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \mathbf{C}^{\rho_1}_\mathrm{m}\;
       \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}

Performing the same procedure for a two axis testbed :math:`(A=2)` and a three axis testbed :math:`(A=3)` gives:

.. math::
	\boldsymbol{r}^\mathrm{i}_{\mathrm{i}b}(t)
	&= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \boldsymbol{r}^\mathrm{n}_{\mathrm{n}{\zeta_2}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_2}\;
       \boldsymbol{r}^{\zeta_2}_{{\zeta_2}{\mu_2}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
       \boldsymbol{r}^{\rho_2}_{{\rho_2}{\zeta_1}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
 	   \mathbf{C}^{\rho_2}_{\zeta_1}\;
       \boldsymbol{r}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
 	   \mathbf{C}^{\rho_2}_{\zeta_1}\;
	   \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
	   \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
 	   \mathbf{C}^{\rho_2}_{\zeta_1}\;
	   \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
	   \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \mathbf{C}^{\rho_1}_\mathrm{m}\;
       \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}

and

.. math::
	\boldsymbol{r}^\mathrm{i}_{\mathrm{i}b}(t)
	&= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \boldsymbol{r}^\mathrm{n}_{\mathrm{n}{\zeta_3}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
       \boldsymbol{r}^{\zeta_3}_{{\zeta_3}{\mu_3}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
	   \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
	   \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
       \boldsymbol{r}^{\rho_3}_{{\rho_3}{\zeta_2}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
	   \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
	   \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
 	   \mathbf{C}^{\rho_3}_{\zeta_2}\;
       \boldsymbol{r}^{\zeta_2}_{{\zeta_2}{\mu_2}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
	   \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
	   \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
 	   \mathbf{C}^{\rho_3}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
       \boldsymbol{r}^{\rho_2}_{{\rho_2}{\zeta_1}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
	   \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
	   \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
 	   \mathbf{C}^{\rho_3}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
 	   \mathbf{C}^{\rho_2}_{\zeta_1}\;
       \boldsymbol{r}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t)\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
	   \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
	   \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
  	   \mathbf{C}^{\rho_3}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
 	   \mathbf{C}^{\rho_2}_{\zeta_1}\;
	   \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
	   \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}}\\\notag
	&+ \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\;
       \mathbf{C}^\mathrm{e}_\mathrm{n}\;
       \mathbf{C}^\mathrm{n}_{\zeta_3}\;
	   \mathbf{C}^{\zeta_3}_{\mu_3}(t)\;
	   \mathbf{C}^{\mu_3}_{\rho_3}(t)\;
  	   \mathbf{C}^{\rho_3}_{\zeta_2}\;
	   \mathbf{C}^{\zeta_2}_{\mu_2}(t)\;
	   \mathbf{C}^{\mu_2}_{\rho_2}(t)\;
 	   \mathbf{C}^{\rho_2}_{\zeta_1}\;
	   \mathbf{C}^{\zeta_1}_{\mu_1}(t)\;
	   \mathbf{C}^{\mu_1}_{\rho_1}(t)\;
       \mathbf{C}^{\rho_1}_\mathrm{m}\;
       \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}

Like with the angular rate, the progression continues for any positive number of testbed axes and a pattern is identified. If we define the following:

.. math::
    \mathbf{C}^{\zeta_1}_{\rho_1}(t) &= \mathbf{C}^{\zeta_1}_{\mu_1}(t)\; \mathbf{C}^{\mu_1}_{\rho_1}(t)\\[1em]
    \mathbf{C}^{\zeta_2}_{\rho_2}(t) &= \mathbf{C}^{\zeta_2}_{\mu_2}(t)\; \mathbf{C}^{\mu_2}_{\rho_2}(t)\\[1em]
    \mathbf{C}^{\zeta_3}_{\rho_3}(t) &= \mathbf{C}^{\zeta_3}_{\mu_3}(t)\; \mathbf{C}^{\mu_3}_{\rho_3}(t)\\[1em]
    \boldsymbol{\alpha}_0(t) &= \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}} + \mathbf{C}^{\rho_1}_\mathrm{m}\; \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}\\[1em]
    \boldsymbol{\alpha}_1(t) &= \boldsymbol{r}^\mathrm{h}_{\mathrm{h}{\zeta_1}} + \mathbf{C}^\mathrm{h}_{\zeta_1} \left[\boldsymbol{r}^{\zeta_1}_{{\zeta_1}{\mu_1}}(t) + \mathbf{C}^{\zeta_1}_{\rho_1}(t)\; \boldsymbol{\alpha}_0(t)\right]\\[1em]
    \boldsymbol{\alpha}_2(t) &= \boldsymbol{r}^\mathrm{h}_{\mathrm{h}{\zeta_2}} + \mathbf{C}^\mathrm{h}_{\zeta_2} \left[\boldsymbol{r}^{\zeta_2}_{{\zeta_2}{\mu_2}}(t) + \mathbf{C}^{\zeta_2}_{\rho_2}(t)\; \boldsymbol{\alpha}_1(t)\right]\\[1em]
    \boldsymbol{\alpha}_3(t) &= \boldsymbol{r}^\mathrm{h}_{\mathrm{h}{\zeta_3}} + \mathbf{C}^\mathrm{h}_{\zeta_3} \left[\boldsymbol{r}^{\zeta_3}_{{\zeta_3}{\mu_3}}(t) + \mathbf{C}^{\zeta_3}_{\rho_3}(t)\; \boldsymbol{\alpha}_2(t)\right]

the three angular rate equations simplify to:

.. math::
    \boldsymbol{r}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) &= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\alpha}_1(t)\\[1em]
    \boldsymbol{r}^\mathrm{i}_{\mathrm{i}b}(t) &= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\alpha}_2(t)\\[1em]
    \boldsymbol{r}^\mathrm{i}_{\mathrm{i}b}(t) &= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\alpha}_3(t)

and the linear position of of a general testbed :math:`(A>0)` is calculated as:

.. math::
    \mathbf{C}^{\zeta_a}_{\rho_a}(t) &= \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\[1em]
    \boldsymbol{\alpha}_0(t) &= \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}} + \mathbf{C}^{\rho_1}_\mathrm{m}\; \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}\\[1em]
    \boldsymbol{\alpha}_a(t) &= \boldsymbol{r}^\mathrm{h}_{\mathrm{h}{\zeta_a}} + \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{r}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t)\right]\\[1em]
	\boldsymbol{r}^\mathrm{i}_{\mathrm{i}b}(t) &= \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}} + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\alpha}_A(t)

Linear Acceleration
===================
The linear acceleration of a general testbed is produced by applying the sum and product rules to the linear position equations twice to provide:

.. math::
    \mathbf{C}^{\zeta_a}_{\rho_a}(t) &= \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\[1em]
    \dot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t) &= \dot{\mathbf{C}}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t) + \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \dot{\mathbf{C}}^{\mu_a}_{\rho_a}(t)\\[1em]
    \ddot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t) &= \ddot{\mathbf{C}}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t) + 2\; \dot{\mathbf{C}}^{\zeta_a}_{\mu_a}(t)\; \dot{\mathbf{C}}^{\mu_a}_{\rho_a}(t) + \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \ddot{\mathbf{C}}^{\mu_a}_{\rho_a}(t)\\[1em]
    \boldsymbol{\alpha}_0(t) &= \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}} + \mathbf{C}^{\rho_1}_\mathrm{m}\; \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}\\[1em]
    \dot{\boldsymbol{\alpha}}_0(t) &= 0\\[1em]
    \ddot{\boldsymbol{\alpha}}_0(t) &= 0\\[1em]
    \boldsymbol{\alpha}_a(t) &= \boldsymbol{r}^\mathrm{h}_{\mathrm{h}{\zeta_a}} + \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{r}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t)\right]\\[1em]
    \dot{\boldsymbol{\alpha}}_a(t) &= \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{v}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \dot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \dot{\boldsymbol{\alpha}}_{a-1}(t)\right]\\[1em]
    \ddot{\boldsymbol{\alpha}}_a(t) &= \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{a}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \ddot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t) + 2\; \dot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t)\; \dot{\boldsymbol{\alpha}}_{a-1}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \ddot{\boldsymbol{\alpha}}_{a-1}(t)\right]\\[1em]
	\boldsymbol{a}^\mathrm{i}_{\mathrm{i}b}(t)
    &= \ddot{\mathbf{C}}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}}
    + \ddot{\mathbf{C}}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\alpha}_A(t)
    + 2\; \dot{\mathbf{C}}^\mathrm{i}_\mathrm{n}(t)\; \dot{\boldsymbol{\alpha}}_A(t)
    + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \ddot{\boldsymbol{\alpha}}_A(t)

We can then apply the `DCM Derivatives <frames.html#derivatives>`_ to produces the final linear acceleration equations:

.. math::
    \mathbf{C}^{\zeta_a}_{\rho_a}(t) &= \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\[1em]
    \dot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t) &= \boldsymbol{\Omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)
    + \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \boldsymbol{\Omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\[1em]
    \ddot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t) &= \dot{\boldsymbol{\Omega}}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\
    &+ \boldsymbol{\Omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \boldsymbol{\Omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\
    &+ 2\; \boldsymbol{\Omega}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t)\; \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \boldsymbol{\Omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\
    &+ \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \dot{\boldsymbol{\Omega}}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\
    &+ \mathbf{C}^{\zeta_a}_{\mu_a}(t)\; \boldsymbol{\Omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\; \boldsymbol{\Omega}^{\mu_a}_{{\mu_a}{\rho_a}}(t)\; \mathbf{C}^{\mu_a}_{\rho_a}(t)\\[1em]
    \boldsymbol{\alpha}_0(t) &= \boldsymbol{r}^{\rho_1}_{{\rho_1}\mathrm{m}} + \mathbf{C}^{\rho_1}_\mathrm{m}\; \boldsymbol{r}^\mathrm{m}_{\mathrm{m}\mathrm{b}}\\[1em]
    \dot{\boldsymbol{\alpha}}_0(t) &= 0\\[1em]
    \ddot{\boldsymbol{\alpha}}_0(t) &= 0\\[1em]
    \boldsymbol{\alpha}_a(t) &= \boldsymbol{r}^\mathrm{h}_{\mathrm{h}{\zeta_a}} + \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{r}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t)\right]\\[1em]
    \dot{\boldsymbol{\alpha}}_a(t) &= \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{v}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \dot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \dot{\boldsymbol{\alpha}}_{a-1}(t)\right]\\[1em]
    \ddot{\boldsymbol{\alpha}}_a(t) &= \mathbf{C}^\mathrm{h}_{\zeta_a} \left[\boldsymbol{a}^{\zeta_a}_{{\zeta_a}{\mu_a}}(t) + \ddot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t)\; \boldsymbol{\alpha}_{a-1}(t) + 2\; \dot{\mathbf{C}}^{\zeta_a}_{\rho_a}(t)\; \dot{\boldsymbol{\alpha}}_{a-1}(t) + \mathbf{C}^{\zeta_a}_{\rho_a}(t)\; \ddot{\boldsymbol{\alpha}}_{a-1}(t)\right]\\[1em]
	\boldsymbol{a}^\mathrm{i}_{\mathrm{i}b}(t)
    &= \boldsymbol{\Omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\; \boldsymbol{\Omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\; \mathbf{C}^\mathrm{i}_\mathrm{e}(t)\; \boldsymbol{r}^\mathrm{e}_{\mathrm{e}\mathrm{n}}\\
    &+ \boldsymbol{\Omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\; \boldsymbol{\Omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\; \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \boldsymbol{\alpha}_A(t)\\
    &+ 2\; \boldsymbol{\Omega}^\mathrm{i}_{\mathrm{i}\mathrm{e}}(t)\; \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \dot{\boldsymbol{\alpha}}_A(t)\\
    &+ \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \ddot{\boldsymbol{\alpha}}_A(t)

Specific Force
==============
The specific force :math:`(f)` sensed by the system under test resolved in the inertial frame is the sum of the linear acceleration of the body frame and gravitational acceleration.

.. math::
    \boldsymbol{f}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) = \boldsymbol{a}^\mathrm{i}_{\mathrm{i}b}(t) + \mathbf{g}^\mathrm{i}_{\mathrm{i}\mathrm{n}}

Gravity is difficult to measure in the inertial frame. However, it is easy to measure in the local navigation frame.

.. math::
    \mathbf{g}^\mathrm{n}_{\mathrm{i}\mathrm{n}} = \begin{bmatrix}0\\0\\-\mathrm{g}_n\end{bmatrix}

Therefore, the specific force in the inertial frame is:

.. math::
    \boldsymbol{f}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t) = \boldsymbol{a}^\mathrm{i}_{\mathrm{i}b}(t) + \mathbf{C}^\mathrm{i}_\mathrm{n}(t)\; \mathbf{g}^\mathrm{n}_{\mathrm{i}\mathrm{n}}

SUT Inputs
==========

.. math::
    \mathbf{x}^\mathrm{b}_{\mathrm{i}\mathrm{b}}(t) = \mathbf{C}^\mathrm{b}_\mathrm{i}(t)\; \mathbf{x}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)

So

.. math::
    \boldsymbol{\omega}^\mathrm{b}_{\mathrm{i}\mathrm{b}}(t) &= \mathbf{C}^\mathrm{b}_\mathrm{i}(t)\; \boldsymbol{\omega}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)\\[1em]
    \dot{\boldsymbol{\omega}}^\mathrm{b}_{\mathrm{i}\mathrm{b}}(t) &= \mathbf{C}^\mathrm{b}_\mathrm{i}(t)\; \dot{\boldsymbol{\omega}}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)\\[1em]
    \boldsymbol{f}^\mathrm{b}_{\mathrm{i}\mathrm{b}}(t) &= \mathbf{C}^\mathrm{b}_\mathrm{i}(t)\; \boldsymbol{f}^\mathrm{i}_{\mathrm{i}\mathrm{b}}(t)\\[1em]