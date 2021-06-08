Utility Class: Common Calculations
==================================
A ``PhotonUtils`` class with helpful common calculations is included within ``PhotonLib`` to aid teams. This class contains two methods, ``calculateDistanceToTargetMeters()``/``CalculateDistanceToTarget()`` and ``estimateTargetTranslation2d()``/``EstimateTargetTranslation()`` (Java and C++ respectively).

Calculating Distance to Target
------------------------------
If your camera is at a fixed height on your robot and the height of the target is fixed, you can calculate the distance to the target based on your camera's pitch and the :ref:`pitch to the target <docs/programming/photonlib/simple-tracked-target:Retrieving Data from a Photon Tracked Target>`.

.. tabs::
   .. code-tab:: java

      // Constants
      static final double kCameraHeight = 0.51; // meters
      static final double kCameraPitch = 0.436; // radians
      static final double kTargetHeight = 2.44; // meters

      // Get distance to target.
      double distanceMeters = PhotonUtils.calculateDistanceToTargetMeters(
        kCameraHeight, kTargetHeight, kCameraPitch, Math.toRadians(target.getPitch());

   .. code-tab:: c++

      #include <photonlib/PhotonUtils.h>
      #include <units/length.h>
      #include <units/angle.h>

      // Constants
      static constexpr auto kCameraHeight = 0.51_m;
      static constexpr auto kCameraPitch = 0.436_rad;
      static constexpr auto kTargetHeight = 2.44_m;

      // Get distance to target.
      units::meter_t distance = photonlib::PhotonUtils::CalculateDistanceToTarget(
        kCameraHeight, kTargetHeight, kCameraPitch, units::degree_t(target.GetPitch()));

.. note:: The C++ version of PhotonLib uses the Units library. For more information, see `here <https://docs.wpilib.org/en/stable/docs/software/basic-programming/cpp-units.html>`_.

Estimating Translation to Target
--------------------------------
You can get a `translation <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/pose.html#translation>`_ to the target based on the distance to the target (calculated above) and angle to the target (yaw).

.. tabs::
   .. code-tab:: java

      // Calculate a translation from the camera to the target.
      Translation2d translation = PhotonUtils.estimateTargetTranslation2d(
        distanceMeters, Rotation2d.fromDegrees(-target.getYaw()));

   .. code-tab:: c++

      // Calculate a translation from the camera to the target.
      frc::Translation2d translation = photonlib::PhotonUtils::EstimateTargetTranslation(
        distance, frc::Rotation2d(units::degree_t(-target.GetYaw())));

.. note:: We are negating the yaw from the camera from CV (computer vision) conventions to standard mathematical conventions. In standard mathematical conventions, as you turn counter-clockwise, angles become more positive.

Estimating Field Relative Pose
------------------------------
You can get your robot's ``Pose2D`` on the field using various camera data, target yaw, gyro angle, target pose, and camera position. This method estimates the target's relative position using ``estimateCameraToTargetTranslation`` (which uses pitch and yaw to estimate range and heading), and the robot's gyro to estimate the rotation of the target.

.. tabs::
   .. code-tab:: java

      // Calculate robot's field relative pose
      Pose2D robotPose = PhotonUtils.estimateFieldToRobot(
        kCameraHeight, kTargetHeight, kCameraPitch, kTargetPitch, Rotation2d.fromDegrees(-target.getYaw()), gyro.getRotation2d(), targetPose, cameraToRobot);

   .. code-tab:: c++

      // Calculate robot's field relative pose
      frc::Pose2D robotPose = photonlib::EstimateFieldToRobot(
        kCameraHeight, kTargetHeight, kCameraPitch, kTargetPitch, frc::Rotation2d(units::degree_t(-target.GetYaw())), frc::Rotation2d(units::degree_t(gyro.GetRotation2d)), targetPose, cameraToRobot);
