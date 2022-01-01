Calibrating Your Camera
=======================

In order to use :ref:`3d mode <docs/getting-started/pipeline-tuning/3D:3D Tuning>`, your camera must be calibrated at the desired resolution. This calibration process must be repeated for each resolution at which users wish to use 3D mode.

To calibrate a camera, images of a chessboard (or grid of dots) are taken. by comparing where the grid corners (or dots) should be in object space (for example, a dot once every inch in an 8x6 grid) with where they appear in the camera image, we can find a least-squares estimate for intrinsic camera properties like focal lengths, center point, and distortion coefficients. For more on camera calibration, please review the `OpenCV documentation <https://docs.opencv.org/4.x/dc/dbb/tutorial_py_calibration.html>`_.

.. warning:: While any resolution can be calibrated, resolutions lower than 960x720 are often too low to provide accurate results.

.. note::The calibration data collected during calibration is specific to each physical camera, as well as each individual resolution.

Calibration with PhotonVision
-----------------------------

The Cameras tab of the UI houses PhotonVision's camera calibration tooling. It assists users with calibrating their cameras, as well as allows them to view previously calibrated resolutions. We support both dot- and chessboard calibrations.

In the Camera Calibration tab, we'll print out the calibration target using the "Download" button. This should be printed on 8.5x11 printer paper. This page shows using an 8x8 chessboard.

.. warning:: Ensure that there is no scaling applied during printing (it should be at 100%) and that the PDF is printed as is on regular printer paper. Check the square size with calibers or an accurate measuring device after printing to ensure squares are sized properly. For optimal results, various resources are available online to calibrate your specific printer if needed.

We'll next select a resolution to calibrate and populate our pattern spacing and board size. The provided chessboard is 8 squares in width and height, and each square should be about 1in across. Mine measured with a caliper was 0.96in, but this will vary per printer. Finally, once our entered data is correct, we'll click "start calibration."

Now, we'll capture images of our chessboard from various angles. The most important part of this step is to make sure that the chessboard overlay matches the chessboard in your image. The further the overdrawn points are from the true position of the chessboard corners, the less accurate the final calibration will be. We'll want to capture at least 12 images, trying to take one in each region of the camera sensor. Once we've got our images, we'll click "Finish calibration" and wait for the calibration process to complete. If all goes well, the mean error and standard deviation will be shown in the table on the right.

.. raw:: html

        <video width="85%" controls>
            <source src="../../../_static/assets/calibration_small.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

For advanced users, these calibrations can be later accessed by :ref:`exporting your config directory <docs/hardware/config:Directory Structure>` and viewing the camera's config.json file. Furthermore, the most recent snapshots will be saved to the calibImgs directory.

.. image:: images/calibImgs.png
   :width: 600
   :alt: Captured calibration images
