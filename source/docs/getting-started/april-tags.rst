AprilTags
=========

.. image:: assets/apriltag.png
   :align: center
   :scale: 20 %

.. important:: For the 2023 FRC Game, FIRST HQ has announced that visual fiducial markers (AprilTags) will be used on the field in addition to retroreflective tape. More information can be found in the `blog post here <https://www.firstinspires.org/robotics/frc/blog/2022-control-system-reporting-2023-updates-and-beta-testing>`_. Get ahead of the game by setting up PhotonVision and start detecting AprilTags in the offseason so you're ready for whatever the 2023 game has to offer!

About AprilTags
^^^^^^^^^^^^^^^

AprilTags are a type of visual fiducial marker that is commonly used within robotics and computer vision applications. Visual fiducial markers are artificial landmarks added to a scene to allow "localization" (finding your current position) via images. In simpler terms, it is something that can act as a known point of reference that you can use to find your current location. They are similar to QR codes in which they encode information, however, they hold much less data. This has the added benefit of being much easier to track from long distances and at low resolutions. By placing AprilTags in known locations around the field and detecting them using PhotonVision, you can easily get full field localization / pose estimation. Alternatively, you can use AprilTags the same way you used retroreflective tape, simply using them to turn to goal without any pose estimation.

A more technical explanation can be found in the `WPILib documentation <https://docs.wpilib.org/en/latest/docs/software/vision-processing/apriltag/apriltag-intro.html>`_.

.. note:: You can get FIRST's `official PDF of the targets used in 2023 here <https://firstfrc.blob.core.windows.net/frc2023/FieldAssets/TeamVersions/AprilTags-UserGuideandImages.pdf>`_.

Getting Started With AprilTags
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1. Install PhotonVision, wire your coprocessor, and get the dashboard up.

.. note:: When selecting the image during installation, ensure you use one from the 2022 beta or 2023 stable release.

2. Read the documentation in the :ref:`pipeline tuning section<docs/getting-started/pipeline-tuning/apriltag-tuning:Target Family>` about how to tune a pipeline for AprilTags.

3. Read page on :ref:`Robot Integration Strategies with AprilTags<docs/integration/aprilTagStrategies:Simple Strategies>` on different approaches to using the data you get from AprilTags. This includes simply turning to the goal, getting the pose of the target, all the way to real-time, latency compensated pose estimation.

4. Read the :ref:`PhotonLib documentation<docs/programming/photonlib/getting-target-data:Getting AprilTag Data From A Target>` on how to use AprilTag data in your code.
