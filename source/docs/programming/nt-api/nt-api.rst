NetworkTables API
=================

More advanced users may want to create their own NetworkTables entries to retrieve data instead of using :ref:`PhotonLib <docs/programming/photonlib/index:PhotonLib: Robot Code Interface>`. However, it is recommended for most users to use PhotonLib as it simplifies the user code experience.

The tables below contain the the name of the key for each entry that PhotonVision sends over the network and a short description of the key. The entries should be extracted from a subtable with your camera's nickname (visible in the PhotonVision UI) under the main ``photonvision`` table.

Getting Target Information
--------------------------
+-------------------+--------------+--------------------------------------------------------------------------+
|        Key        |     Type     |                               Description                                |
+===================+==============+==========================================================================+
| ``rawBytes``      | ``byte[]``   | A byte-packed string that contains target info from the same timestamp.  |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``latencyMillis`` | ``double``   | The latency of the pipeline in milliseconds.                             |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``hasTarget``     | ``boolean``  | Whether the pipeline is detecting targets or not.                        |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``targetPitch``   | ``double``   | The pitch of the target in degrees (positive up).                        |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``targetYaw``     | ``double``   | The yaw of the target in degrees (positive right).                       |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``targetArea``    | ``double``   | The area (percent of bounding box in screen) as a percent (0-100).       |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``targetSkew``    | ``double``   | The skew of the target in degrees (counter-clockwise positive).          |
+-------------------+--------------+--------------------------------------------------------------------------+
| ``targetPose``    | ``double[]`` | The pose of the target relative to the robot (x, y, rotation in degrees) |
+-------------------+--------------+--------------------------------------------------------------------------+

Changing Settings
-----------------
+-------------------+-------------+-----------------------------+
|        Key        |    Type     |         Description         |
+===================+=============+=============================+
| ``pipelineIndex`` | ``int``     | Changes the pipeline index. |
+-------------------+-------------+-----------------------------+
| ``driverMode``    | ``boolean`` | Toggles driver mode.        |
+-------------------+-------------+-----------------------------+


Saving Images
-----------------
PhotonVision can save images to file on command. The image is saved when PhotonVision detects the command went from ``false`` to ``true``.

PhotonVision will automatically set these back to ``false`` after 500ms.

Be careful saving images rapidly - it will slow vision processing performance and take up disk space very quickly.

Images are returned as part of the .zip package from the "Export" operation in the Settings tab.

+----------------------+-------------+----------------------------------------------------+
|         Key          |    Type     |                     Description                    |
+======================+=============+====================================================+
| ``inputSaveImgCmd``  | ``boolean`` | Triggers saving the current input image to file.   |
+----------------------+-------------+----------------------------------------------------+
| ``outputSaveImgCmd`` | ``boolean`` | Triggers saving the current output image to file.  |
+----------------------+-------------+----------------------------------------------------+

.. warning:: If you manage to make calls to these commands faster than 500ms (between calls), additional photos will not be captured.

Global Entries
--------------
These entries are global, meaning that they should be called on the main ``photonvision`` table.

+-------------+---------+----------------------------------------------------------+
|     Key     |  Type   |                       Description                        |
+=============+=========+==========================================================+
| ``ledMode`` | ``int`` | Sets the LED Mode (-1: default, 0: off, 1: on, 2: blink) |
+-------------+---------+----------------------------------------------------------+

.. warning::
   Setting the LED mode to -1 (default) when `multiple` cameras are connected may result in unexpected behavior. :ref:`This is a known limitation of PhotonVision. <docs/other/known-issues:LED Control>`

   Single camera operation should work without issue.

