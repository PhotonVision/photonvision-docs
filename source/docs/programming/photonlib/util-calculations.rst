Utility Class: Common Calculations
==================================
A ``PhotonUtils`` class with helpful common calculations is included within ``PhotonLib`` to aid teams. This class contains two methods, ``calculateDistanceToTargetMeters()``/``CalculateDistanceToTarget()`` and ``estimateTargetTranslation2d()``/``EstimateTargetTranslation()`` (Java and C++ respectively).

Calculating Distance to Target
------------------------------
If your camera is at a fixed height on your robot and the height of the target is fixed, you can calculate the distance to the target based on your camera's pitch and the :ref:`pitch to the target <docs/programming/photonlib/simple-tracked-target:Retrieving Data from a Photon Tracked Target>`.

.. tabs::

   .. group-tab:: Java

      .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/getinrange/Robot.java
         :language: java
         :lines: 37-42

      .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/getinrange/Robot.java
         :language: java
         :lines: 72-84

   .. group-tab:: C++

      .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/getinrange/include/Robot.h
         :language: cpp
         :lines: 35-41
      
      .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/getinrange/cpp/Robot.cpp
         :language: cpp
         :lines: 34-36	  

.. note:: The C++ version of PhotonLib uses the Units library. For more information, see `here <https://docs.wpilib.org/en/stable/docs/software/basic-programming/cpp-units.html>`_.

Estimating Camera Translation to Target
---------------------------------------
You can get a `translation <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/pose.html#translation>`_ to the target based on the distance to the target (calculated above) and angle to the target (yaw).

.. tabs::
   .. code-tab:: java

      // Calculate a translation from the camera to the target.
      Translation2d translation = PhotonUtils.estimateCameraToTargetTranslation(
        distanceMeters, Rotation2d.fromDegrees(-target.getYaw()));

   .. code-tab:: c++

      // Calculate a translation from the camera to the target.
      frc::Translation2d translation = photonlib::PhotonUtils::EstimateCameraToTargetTranslationn(
        distance, frc::Rotation2d(units::degree_t(-target.GetYaw())));

.. note:: We are negating the yaw from the camera from CV (computer vision) conventions to standard mathematical conventions. In standard mathematical conventions, as you turn counter-clockwise, angles become more positive.
