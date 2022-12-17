Using WPILib Pose Estimation, Simulation, and PhotonVision Together
===================================================================

The following example comes from the PhotonLib example repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/>`_).  Full code is available at that links.

Knowledge and Equipment Needed
-----------------------------------------------

- Everything required in :ref:`Combining Aiming and Getting in Range <docs/examples/aimandrange:Knowledge and Equipment Needed>`, plus some familiarity with WPILib pose estimation functionality.

Background
----------

This example builds upon WPILib's `Differential Drive Pose Estimator <https://github.com/wpilibsuite/allwpilib/tree/main/wpilibjExamples/src/main/java/edu/wpi/first/wpilibj/examples/differentialdriveposeestimator>`_. It adds a :code:`PhotonCamera` to gather estimates of the robot's position on the field. This in turn can be used for aligning with vision targets, and increasing accuracy of autonomous routines.

To support simulation, a :code:`SimVisionSystem` is used to drive data into the :code:`PhotonCamera`. The far high goal target from 2020 is modeled.

Walkthrough
-----------

WPILib's :code:`Pose2d` class is used to represent robot positions on the field.

Three different :code:`Pose2d` positions are relevant for this example:

1) Desired Pose: The location the some autonomous routine wants the robot to be in.
2) Estimated Pose: The location the software `believes` the robot to be in, based on physics models and sensor feedback.
3) Actual Pose: The locations he robot is actually at. The physics simulation generates this in simulation, but it cannot be directly measured on the real robot.

Estimating Pose
^^^^^^^^^^^^^^^

The :code:`DrivetrainPoseEstimator` class is responsible for generating an estimated robot pose using sensor readings (including PhotonVision).

Please reference the `WPILib documentation <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/state-space/state-space-pose_state-estimators.html>`_ on using the :code:`DifferentialDrivePoseEstimator` class.

For both simulation and on-robot code, we create objects to represent the physical location and size of the vision targets we are calibrated to detect. This example models the down-field high goal vision target from the 2020 and 2021 games.

.. tab-set::

    .. tab-item:: Java
       :sync: java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/robot/Constants.java
         :language: java
         :lines: 79-101
         :linenos:
         :lineno-start: 79


    .. tab-item:: C++
       :sync: cpp

       :code:`//Coming soon!`

To incorporate Photon Vision, we need to create a :code:`PhotonCamera`:

.. tab-set::

    .. tab-item:: Java
       :sync: java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/robot/DrivetrainPoseEstimator.java
         :language: java
         :lines: 49
         :linenos:
         :lineno-start: 49


    .. tab-item:: C++
       :sync: cpp

       :code:`//Coming soon!`

During periodic execution, we read back camera results. If we see a target in the image, we pass the camera-measured pose of the robot to the :code:`DifferentialDrivePoseEstimator`.

.. tab-set::

    .. tab-item:: Java
       :sync: java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/robot/DrivetrainPoseEstimator.java
         :language: java
         :lines: 82-94
         :linenos:
         :lineno-start: 82


    .. tab-item:: C++
       :sync: cpp

       :code:`//Coming soon!`

That's it!

Simulating the Camera
^^^^^^^^^^^^^^^^^^^^^

First, we create a new :code:`SimVisionSystem` to represent our camera and coprocessor running PhotonVision.

.. tab-set::

    .. tab-item:: Java
       :sync: java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/sim/DrivetrainSim.java
         :language: java
         :lines: 77-98
         :linenos:
         :lineno-start: 77


    .. tab-item:: C++
       :sync: cpp

       :code:`//Coming soon!`

Then, we add our target to the simulated vision system.

.. tab-set::

    .. tab-item:: Java
       :sync: java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/sim/DrivetrainSim.java
         :language: java
         :lines: 100-102
         :linenos:
         :lineno-start: 100


    .. tab-item:: C++
       :sync: cpp

       :code:`//Coming soon!`

If you have additional targets you want to detect, you can add them in the same way as the first one.


Updating the Simulated Vision System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once we have all the properties of our simulated vision system defined, the remaining work is minimal. Periodically, pass in the robot's pose to the simulated vision system.

.. tab-set::

    .. tab-item:: Java
       :sync: java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/sim/DrivetrainSim.java
         :language: java
         :lines: 141-142
         :linenos:
         :lineno-start: 141


    .. tab-item:: C++
       :sync: cpp

       :code:`//Coming soon!`

The rest is done behind the scenes.



