Simple Tracked Target
=====================

What is a Simple Tracked Target?
--------------------------------
A simple tracked target contains information about each target from a :ref:`pipeline result <docs/photonlib/simple-pipeline-result:Simple Pipeline Result>`. This information includes yaw, pitch, area, and robot relative pose.

Retrieving Data from a Simple Tracked Target
--------------------------------------------
You can use the ``getYaw()``/``GetYaw()``, ``getPitch()``/``GetPitch()``, ``getArea()``/``GetArea()``, and ``getRobotRelativePose()``/``GetRobotRelativePose()`` methods (Java and C++ respectively) within the tracked target class to retrieve the yaw, pitch, area and robot-relative pose of the target.

.. tabs::
   .. code-tab:: java

      // Get information from target.
      double yaw = target.getYaw();
      double pitch = target.getPitch();
      double area = target.getArea();
      Pose2d pose = target.getRobotRelativePose();

   .. code-tab:: c++

      // Get information from target.
      double yaw = target.GetYaw();
      double pitch = target.GetPitch();
      double area = target.GetArea();
      frc::Pose2d pose = target.GetRobotRelativePose();

.. note:: The units for yaw and pitch are degrees and use standard computer vision directionality. Therefore, a negative yaw means that the recognized target is to the left of the center of the screen and a negative pitch means that the recognized target is below the center of the screen.

.. note:: The robot relative pose returns the pose of the target in a coordinate frame where the robot is the origin and the heading of the robot is along the x-axis. For more information about the ``Pose2d`` class, see `here <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/pose.html#pose>`_.
