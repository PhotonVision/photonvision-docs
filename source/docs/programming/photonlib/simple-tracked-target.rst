Photon Tracked Target
=====================

What is a Photon Tracked Target?
--------------------------------
A tracked target contains information about each target from a :ref:`pipeline result <docs/programming/photonlib/simple-pipeline-result:Photon Pipeline Result>`. This information includes yaw, pitch, area, and robot relative pose.

Retrieving Data from a Photon Tracked Target
--------------------------------------------
You can use the ``getYaw()``/``GetYaw()``, ``getPitch()``/``GetPitch()``, ``getArea()``/``GetArea()``, ``getSkew()``/``GetSkew()``,and ``getCameraToTarget()``/``GetCameraToTarget()`` methods (Java and C++ respectively) within the tracked target class to retrieve the yaw, pitch, area, skew, and the camera-to-target transform.

.. tabs::
   .. code-tab:: java

      // Get information from target.
      double yaw = target.getYaw();
      double pitch = target.getPitch();
      double area = target.getArea();
      double skew = target.getSkew();
      Transform2d pose = target.getCameraToTarget();

   .. code-tab:: c++

      // Get information from target.
      double yaw = target.GetYaw();
      double pitch = target.GetPitch();
      double area = target.GetArea();
      double skew = target.GetSkew();
      frc::Transform2d pose = target.GetCameraToTarget();

.. note:: The units for yaw, pitch, and skew are degrees and use standard computer vision directionality. Therefore, a negative yaw means that the recognized target is to the left of the center of the screen, a negative pitch means that the recognized target is below the center of the screen, and skew values are counter-clockwise-positive measured with respect to the horizontal (taking portrait/landscape mode into account). Furthermore, area is scaled from 0-100, representing the percentage of the screen taken up by the bounding box.

.. note:: The camera-to-target transform represents a 2d transformation (translation and rotation) to the target. For more information on how this works, please see the `2d transform documentation <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/transformations.html#transform2d-and-twist2d>`_.
