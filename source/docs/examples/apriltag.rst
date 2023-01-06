Using AprilTags for Pose Estimation
===================================

The following example is from the PhotonLib example repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/apriltagExample>`_).


Knowledge and Equipment Needed
------------------------------

- Everything required in :ref:`Aiming at a Target <docs/examples/aimingatatarget:Knowledge and Equipment Needed>`.
- Large space where your robot can move around freely
- An open space with properly mounted 16h5 AprilTags
- PhotonVision running on your laptop or a coprocessor

This is example will show how to use AprilTags for full field robot localization using ``RobotPoseEstimator``, ``AprilTagFieldLayout``, and the WPILib Pose Estimaton Classes.

All PhotonVision specific code is in ``PhotonCameraWrapper.java`` and the relevant pose estimation parts are in ``DriveTrain.java.``

Please note that this code does not support simulation in the traditional sense (properly simulating each target that can be detected within sim), but you can still see the pose the camera is returning from the tags using Glass / Field2d when you are running PhotonVision on a robot. Make sure you properly set your ip/hostname in ``Robot.java`` when doing this.  