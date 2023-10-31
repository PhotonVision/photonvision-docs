Simulating Aiming and Getting in Range
======================================

The following example comes from the PhotonLib example repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/simaimandrange>`_). Full code is available at that link.

.. raw:: html

   <video width="85%" controls>
      <source src="../../_static/assets/simaimandrange.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

.. attention:: A C++ example does not currently exist.

Background
----------

The previous examples show how to use PhotonVision on a real robot, with the robot code making use of PhotonVision data published by a coprocessor to move a physical drivetrain.

This example showcases simulation support added to the previous :ref:`docs/examples/aimandrange:combining aiming and getting in range` example. This means both the physical drivetrain and PhotonVision data can be simulated on your development computer, and you can test your robot code without a real robot. See :ref:`docs/programming/photonlib/simulation:simulation support in photonlib` for more info on PhotonVision simulation.

Walkthrough
-----------

Defining used hardware
^^^^^^^^^^^^^^^^^^^^^^

Inheriting from the ``aimandrange`` example, we have some basic setup in our ``Robot`` class:

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/Robot.java
      :language: java
      :lines: 46-59
      :linenos:
      :lineno-start: 46

In the ``Robot`` class, we also add support to periodically update new simulation-specific objects. This logic only gets used while running in simulation, and is where we will handle simulating the field, robot, and camera:

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/Robot.java
      :language: java
      :lines: 108-124
      :linenos:
      :lineno-start: 108

Simulating the Drivetrain
^^^^^^^^^^^^^^^^^^^^^^^^^

We implement our new ``DrivetrainSim`` class so we can drive the robot in simulation. Please reference the `WPILib documentation on physics simulation <https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html>`_.

This drivetrain simulation is defined by the properties provided in the ``Constants`` class:

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/Constants.java
      :language: java
      :lines: 73-90
      :linenos:
      :lineno-start: 73

To put it simply, this class will take in the drivetrain inputs (the percentage outputs commanded to the left and right side motors of our differential drivetrain) and simulate the drivetrain dynamics, or how it should respond.

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/sim/DrivetrainSim.java
      :language: java
      :lines: 72-90
      :linenos:
      :lineno-start: 72

Simulating the Vision System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``VisionSim`` class will handle simulating the vision targets on the field and what our camera should see, as well as publishing data to NetworkTables to mimic an actual coprocessor running PhotonVision. For more information on PhotonVision simulation, see :ref:`docs/programming/photonlib/simulation:simulation support in photonlib`.

This class revolves around a ``VisionSystemSim`` and ``PhotonCameraSim``. These handle simulating the field and camera data, respectively.

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/sim/VisionSim.java
      :language: java
      :lines: 77-80
      :linenos:
      :lineno-start: 77

We'll start by modeling the shape of the vision target we will put on the field (the 2020 High Goal target):

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/sim/VisionSim.java
      :language: java
      :lines: 52-62
      :linenos:
      :lineno-start: 52

`...` and create a ``VisionTargetSim`` with where the target is on the field, which will be put in the ``VisionSystemSim``:

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/sim/VisionSim.java
      :language: java
      :lines: 82-86
      :linenos:
      :lineno-start: 82

Now, we can create our camera simulation to view the simulated field. The camera simulation is defined by the given properties:

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/sim/VisionSim.java
      :language: java
      :lines: 64-75
      :linenos:
      :lineno-start: 64

`...` and added to the ``VisionSystemSim``. The ``Transform3d`` used describes where the camera is on the robot.

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/sim/VisionSim.java
      :language: java
      :lines: 88-104
      :linenos:
      :lineno-start: 88

Viewing the Simulation World
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once we have all the properties of our simulated drivetrain and vision system defined, the work to do at runtime becomes very minimal. As mentioned at the start, we simply pass in the simulated robot's pose periodically to the simulated vision system in the ``Robot`` class:

.. tab-set-code::

   .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/v2024.1.1-beta-1/photonlib-java-examples/simaimandrange/src/main/java/frc/robot/Robot.java
      :language: java
      :lines: 108-124
      :linenos:
      :lineno-start: 108

The rest is done behind the scenes.

Simulating the project will open the simgui tool, where a Field2d shows a top-down view of the robot, camera, and vision target poses. The camera stream is also simulated and made available similar to an actual coprocessor running PhotonVision. This can be seen in Shuffleboard or a browser (for our single simulated camera, the input stream should be at ``localhost:1181`` and output stream at ``localhost:1182``). Both of these are showcased in the video at the top of this page.
