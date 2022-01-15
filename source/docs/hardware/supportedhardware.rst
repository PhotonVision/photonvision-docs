Supported Hardware
==================

PhotonVision is developed and tested on a number of Commercial, Off-the-Shelf vision processing hardware solutions.

Supported Cameras
-----------------
* Pi Camera Module V1 and V2

  * The V1 is strongly preferred over the V2 due to the V2 having undesirable FOV choices.

* USB Cameras

  * Recommended: Microsoft LifeCam HD-3000 (available from AndyMark)

  * Most Logitech cameras (specifically the Logitech C270 HD Webcam (PN: 960-000694)) will not work with PhotonVision. The PS3Eye needs a workaround to be usable, for more information see :ref:`our Known Issues page <docs/other/known-issues:Hardware Issues>`

* ELP Cameras

Supported Coprocessors
----------------------
* Raspberry Pi 3 (any version)
* Raspberry Pi 4 (any version)

Recommended Hardware Combinations
---------------------------------
The following combinations are ranked from best to worst:

1. Raspberry Pi 3 with Pi Camera
2. Raspberry Pi 4 with Pi Camera
3. Raspberry Pi 4 with USB Camera
4. Raspberry Pi 3 with USB Camera

GPU Acceleration
----------------
PhotonVision uses GPU Acceleration in order to maximize processing performance, however it is only supported on the Raspberry Pi 3, which is why it is recommended over the Pi 4. For the technical information on why it is not supported on the Raspberry Pi 4, please see `here. <https://www.chiefdelphi.com/t/announcing-gloworm-an-inexpensive-and-open-source-vision-module/386370/61?u=pietroglyph>`_


Support Levels
--------------
.. list-table::
   :widths: 15 30 45
   :header-rows: 1

   * - Support Level
     - Support Qualities
     - Hardware
   * - Fully Supported
     -   * Full discord help
         * All features will work
         * Everything will be kept up to date
     -   * Gloworm
         * Raspberry Pi 3 and Raspberry Pi 4 with the official Pi image with the Pi Cam or USB Cameras
   * - Compatible
     -   * No guarantee of support on Discord
         * Major features will work
         * We hope to keep things up to date
     -   * Linux (aarch64, armv7, x86_64)
         * Windows (x86_64)
   * - Unsupported
     -   * Told to use something else
         * Won't try to make these work/update them
         * No guarantees
     -   * macOS
         * Anything not listed above

Vendors
-------
* Gloworm

  * `Website/Documentation <https://gloworm.vision/>`__

  * `Image <https://github.com/gloworm-vision/pi-img-updator/releases>`__

  * `Discord <https://discord.com/invite/DncQRky>`__

* SnakeEyes

  * `Website <https://www.playingwithfusion.com/productview.php?pdid=133>`__

  * `Image <https://github.com/PlayingWithFusion/SnakeEyesDocs/releases/latest>`__

  * `Documentation <https://github.com/PlayingWithFusion/SnakeEyesDocs/blob/master/PhotonVision/readme.md>`__
