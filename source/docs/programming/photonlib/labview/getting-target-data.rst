Getting Target Data
===================

Getting The Latest Result
------------------------

Use ``PhotonCamera_GetLatestResult.vi`` to get the latest pipeline result.

.. image:: images/get_latest_result.png


Checking For Targets
--------------------

Check if the pipeline has targets by using ``PhotonPipelineResult_HasTargets?.vi``.

.. image:: images/has_targets.png

``PhotonCamera_GetLatestResult.vi`` will also return if the pipeline has targets.

.. image:: images/has_targets_2.png

Getting an Array of Targets
---------------------------

Each pipeline result will contain an array of targets to get that array use an unbunlde by name node and select targets.

.. image:: images/get_targets.png

Getting The Best Target
-----------------------

``PhotonPipelineResult_GetBestTarget.vi`` will return the best target from a pipeline result.

.. image:: images/get_best_target.png

Getting Target By ID
--------------------

If you are using an april tag pipeline you can use ``PhotonPipelineResult_GetBestTargetById.vi`` to return a target with a specified ID.

.. image:: images/get_target_by_id.png

Getting Target Data
-------------------
* double ``PhotonTrackedTarget_GetYaw.vi``: The yaw of the target in degrees (positive right).
* double ``PhotonTrackedTarget_GetPitch.vi``: The pitch of the target in degrees (positive up).
* double ``PhotonTrackedTarget_GetArea.vi``: The area (how much of the camera feed the bounding box takes up) as a percent (0-100).
* double ``PhotonTrackedTarget_GetSkew.vi``: The skew of the target in degrees (counter-clockwise positive).
* double[] ``PhotonTrackedTarget_GetConors.vi``: The 4 corners of the minimum bounding box rectangle.
* Transform2d ``PhotonTrackedTarget_GetBestCameraToTarget.vi``: The camera to target transform. See `2d transform documentation here <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/transformations.html#transform2d-and-twist2d>`_.

.. image:: images/get_data.png