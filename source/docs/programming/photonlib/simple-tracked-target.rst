Simple Tracked Target
=====================

What is a Simple Tracked Target?
--------------------------------
A simple tracked target contains information about each target from a :ref:`pipeline result <docs/programming/photonlib/simple-pipeline-result:Simple Pipeline Result>`. This information includes yaw, pitch, area, and robot relative pose.

Retrieving Data from a Simple Tracked Target
--------------------------------------------
You can use the ``getYaw()``/``GetYaw()``, ``getPitch()``/``GetPitch()``, ``getArea()``/``GetArea()``, ``getSkew()``/``GetSkew()``,and ``getRobotRelativePose()``/``GetRobotRelativePose()`` methods (Java and C++ respectively) within the tracked target class to retrieve the yaw, pitch, area, skew, and robot-relative pose of the target.

.. tabs::
   .. code-tab:: java

      // Get information from target.
      double yaw = target.getYaw();
      double pitch = target.getPitch();
      double area = target.getArea();
      double skew = target.getSkew();
      Pose2d pose = target.getRobotRelativePose();

   .. code-tab:: c++

      // Get information from target.
      double yaw = target.GetYaw();
      double pitch = target.GetPitch();
      double area = target.GetArea();
      double skew = target.GetSkew();
      frc::Pose2d pose = target.GetRobotRelativePose();

.. note:: The units for yaw, pitch, and skew are degrees and use standard computer vision directionality. Therefore, a negative yaw means that the recognized target is to the left of the center of the screen, a negative pitch means that the recognized target is below the center of the screen, and skew values are counter-clockwise-positive measured with respect to the horizontal (taking portrait/landscape mode into account). Furthermore, area is scaled from 0-100, representing the percentage of the screen taken up by the bounding box.

.. note:: The robot relative pose returns the pose of the target in a coordinate frame where the robot is the origin and the heading of the robot is along the x-axis. For more information about the ``Pose2d`` class, see `here <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/pose.html#pose>`_.
