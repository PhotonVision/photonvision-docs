About Fiducials / April Tags
============================

|

.. image:: assets/apriltag.png
   :align: center
   :scale: 25 %

| 

Visual fiducials are artificial landmarks / markers added to a scene to facilitate localization between images. In simpler terms, it is something that can act as a known point of reference that you can use to find your current location. They are similar to QR codes in which they encode information, however, they hold much less information (12 bits). This has the added benefit of being much easier to track from long distances and at low resolutions. There are many different types of visual fiducials used in computer vision applications (ARToolKit, ArUco, ARTag, etc.) but PhotonVision utilizes `AprilTags <https://april.eecs.umich.edu/software/apriltag>`_, an open source fiducial library that is popular in robotics. By placing AprilTags in known locations around the field and detecting them using PhotonVision, you can easily get full field localization / pose estimation. This has clear advantages over the traditional method of retroreflective tape based vision, including localization is simplified, tuning is less dependent on the environment, tracking is more robust, easier for teams to construct (don't need expensive tape, just a printer), bright lights are no longer necessary for tracking, it prepares students for industry, and much more.

During the 2022-2023 offseason, PhotonVision is looking for events that are willing to demo AprilTags in order to spread awareness and serve as a proof of concept for potential implementation in future FIRST games.