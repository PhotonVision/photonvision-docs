Simulating Swerve Drive Pose Estimation
=======================================

The following example comes from the PhotonLib example repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/swervedriveposeestsim>`_). Full code is available at that link.

.. raw:: html

   <video width="85%" controls>
      <source src="../../_static/assets/swervedriveposeestsim.mp4" type="video/mp4">
      Your browser does not support the video tag.
   </video>

.. attention:: A C++ example does not currently exist. For a simple pose estimation example in C++ (without sim), see `apriltagExample <https://github.com/PhotonVision/photonvision/tree/master/photonlib-cpp-examples/apriltagExample>`_.

Background
----------

Starting in 2023, :ref:`docs/getting-started/april-tags:apriltags` were added to the FRC field to aid in vision localization. AprilTags can greatly improve the accuracy of pose estimation for teams, which expands autonomous capabilities. This example aims to demonstrate how pose estimation might be done on a swerve drivetrain using PhotonVision for AprilTag detection. For more information on pose estimation, see `Pose Estimators <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/state-space/state-space-pose-estimators.html>`_.

The previous non-simulation examples show how to use PhotonVision on a real robot, with the robot code making use of PhotonVision data published by a coprocessor to move a physical drivetrain. In addition to showcasing pose estimation on a swerve drivetrain, this example shows how all of this can be simulated on your development computer using PhotonLib to get an idea of real-world performance in various scenarios. See :ref:`docs/programming/photonlib/simulation:simulation support in photonlib` for more info on PhotonVision simulation.

Walkthrough
-----------

Project Structure
^^^^^^^^^^^^^^^^^

As a minimal example, this project is a simple ``TimedRobot`` without any command-based functionality used.

The ``SwerveDrive`` Class
~~~~~~~~~~~~~~~~~~~~~~~~~

The ``SwerveDrive`` class contains all the high-level controls and measurements for the swerve drivetrain. It's also where we will track the estimated robot pose with WPILib's ``SwerveDrivePoseEstimator`` and accept vision measurements.

Low-level control is accomplished through the ``SwerveModule`` class, which represents the hypothetical swerve drive's hardware with ``PWMSparkMax`` for motor controllers and ``Encoder`` for encoders. These WPILib classes are used for simplicity over any vendor's library.

The ``Vision`` Class
~~~~~~~~~~~~~~~~~~~~

The ``Vision`` class manages vision data from our coprocessor running PhotonVision. The main functionality of this class is through the ``PhotonPoseEstimator``, which provides pose estimates of the robot based on AprilTags seen by the camera.

The ``Robot`` Class
~~~~~~~~~~~~~~~~~~~

Simulation
^^^^^^^^^^

Simulating the Swerve Drive
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Simulating the Vision System
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Viewing the Simulation World
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
