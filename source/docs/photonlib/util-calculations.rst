Utility Class: Common Calculations
==================================
A ``PhotonUtils`` class with helpful common calculations is included within ``PhotonLib`` to aid teams. This class contains two methods, ``calculateDistanceToTargetMeters()``/``CalculateDistanceToTarget()`` and ``estimateTargetTranslation2d()``/``EstimateTargetTranslation()`` (Java and C++ respectively).

Calculating Distance to Target
------------------------------
If your camera is at a fixed height on your robot and the height of the target is fixed, you can calculate the distance to the target based on your camera's pitch and the :ref:`pitch to the target <docs/photonlib/creating-photon-camera:Getting Yaw, Pitch, and Area>`.

.. tabs::
   .. code-tab:: java

      // Constants
      static final double kCameraHeight = 0.51; // meters
      static final double kCameraPitch = 0.436; // radians
      static final double kTargetHeight = 2.44; // meters

      // Get distance to target.
      double distanceMeters = PhotonUtils.calculateDistanceToTargetMeters(
        kCameraHeight, kTargetHeight, kCameraPitch, Math.toRadians(camera.getFirstTargetPitch());

   .. code-tab:: c++

      #include <photonlib/lib/PhotonUtils.h>
      #include <units/length.h>
      #include <units/angle.h>

      // Constants
      static constexpr auto kCameraHeight = 0.51_m;
      static constexpr auto kCameraPitch = 0.436_rad;
      static constexpr auto kTargetHeight = 2.44_m;

      // Get distance to target.
      units::meter_t distance = photonlib::PhotonUtils::CalculateDistanceToTarget(
        kCameraHeight, kTargetHeight, kCameraPitch, units::degree_t(camera.GetFirstTargetPitch()));

.. note:: The C++ version of PhotonLib uses the Units library. For more information, see `here <https://docs.wpilib.org/en/stable/docs/software/basic-programming/cpp-units.html>`_.

Estimating Translation to Target
--------------------------------
You can get a `translation <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/pose.html#translation>`_ to the target based on the distance to the target (calculated above) and angle to the target (yaw).

.. tabs::
   .. code-tab:: java

      // Calculate a translation from the camera to the target.
      Translation2d translation = PhotonUtils.estimateTargetTranslation2d(
        distanceMeters, Rotation2d.fromDegrees(-camera.getFirstTargetYaw()));

   .. code-tab:: c++

      // Calculate a translation from the camera to the target.
      frc::Translation2d translation = photonlib::PhotonUtils::EstimateTargetTranslation(
        distance, frc::Rotation2d(units::degree_t(-camera.GetFirstTargetYaw())));

.. note:: We are negating the yaw from the camera from CV (computer vision) conventions to standard mathematical conventions. In standard mathematical conventions, as you turn counter-clockwise, angles become more positive.
