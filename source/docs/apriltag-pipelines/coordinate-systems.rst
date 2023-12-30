Coordiante Systems
==================

Field and Robot Coordiante Frame
--------------------------------

PhotonVision follows the WPILib conventions for the robot and field coordinate-systems, as defined `here <https://docs.wpilib.org/en/stable/docs/software/advanced-controls/geometry/coordinate-systems.html>`_.

You define the camera to robot transform in the robot coordinate frame.

Camera Coordinate Frame
-----------------------

The camera coordinate system is defined as follows, relative to the camera sensor itself, and when looking in the same direction as the sensor points:

* The origin is the center.
* The x-axis points to the left
* The y-axis points up.
* The z-axis points out toward the subject.

AprilTag Coordinate Frame
-------------------------

The AprilTag coordinate system is defined as follows, relative to the center of the AprilTag itself, and when viewing the tag as a robot would.=:

* The origin is the center.
* The x-axis points to your right
* The y-axis points upwards.
 * The z-axis is normal to the plane the tag is printed on, pointing outward from the visible side of the tag.

.. image:: images/apriltag-coords.png
   :align: center
   :scale: 50%
   :alt: AprilTag Coordinate System
