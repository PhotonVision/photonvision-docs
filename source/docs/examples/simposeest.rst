Using WPILib Pose Estimation, Simulation, and PhotonVision Together
===================================================================

Background
----------

Full code may be found in the PhotonLib repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest>`_).

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

Specifically, to incorporate Photon Vision, we need to create a :code:`PhotonCamera`:

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/robot/DrivetrainPoseEstimator.java
         :language: java
         :lines: 41
         :linenos:
         :lineno-start: 41

		 
    .. tab-item:: C++

       :code:`//Coming soon!`

Then, during periodic execution, we read back results. If we see a target in the image, we pass the camera-measured pose of the robot to the :code:`DifferentialDrivePoseEstimator`.

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/robot/DrivetrainPoseEstimator.java
         :language: java
         :lines: 67-86
         :linenos:
         :lineno-start: 67

		 
    .. tab-item:: C++

       :code:`//Coming soon!`

That's it!

Simulating the Camera
^^^^^^^^^^^^^^^^^^^^^

First, we create a new :code:`SimVisionSystem` to represent our camera and coprocessor running PhotonVision.

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/sim/DrivetrainSim.java
         :language: java
         :lines: 69-90
         :linenos:
         :lineno-start: 69

		 
    .. tab-item:: C++

       :code:`//Coming soon!`

Next, we create objects to represent the physical location and size of the vision targets we are calibrated to detect. This example models the down-field high goal vision target from the 2020 and 2021 games.

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/robot/Constants.java
         :language: java
         :lines: 71-93
         :linenos:
         :lineno-start: 71

		 
    .. tab-item:: C++

       :code:`//Coming soon!`

Finally, we add our target to the simulated vision system.

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/sim/DrivetrainSim.java
         :language: java
         :lines: 92-94
         :linenos:
         :lineno-start: 92

		 
    .. tab-item:: C++

       :code:`//Coming soon!`

If you have additional targets you want to detect, you can add them in the same way as the first one.


Updating the Simulated Vision System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once we have all the properties of our simulated vision system defined, the work to do at runtime becomes very minimal. Simply pass in the robot's pose periodically to the simulated vision system.

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simposeest/sim/DrivetrainSim.java
         :language: java
         :lines: 133-134
         :linenos:
         :lineno-start: 133

		 
    .. tab-item:: C++

       :code:`//Coming soon!`

The rest is done behind the scenes.



