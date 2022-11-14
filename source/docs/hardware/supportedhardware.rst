Supported Hardware
==================

PhotonVision is developed and tested on a number of Commercial, Off-the-Shelf vision processing hardware solutions.

Supported Cameras
-----------------
PhotonVision works with Pi Cameras and most USB Cameras, the recommendations below are known to be working and have been tested. Other cameras such as webcams, virtual cameras, etc. are not officially supported and may not work. It is important to note that fisheye cameras should only be used as a driver camera and not for detecting targets.

PhotonVision relies on `CSCore <https://github.com/wpilibsuite/allwpilib/tree/main/cscore>`_ to detect and process cameras, so camera support is determined based off compatibility with CScore along with native support for the camera within your OS (ex. `V4L compatibility <https://en.wikipedia.org/wiki/Video4Linux>`_ if using a Linux machine like a Raspberry Pi).

Pi cameras are always recommended over USB cameras as they have lower latency and better performance compared to your average USB Camera.

* `Pi Camera Module V1 <https://www.amazon.com/gp/product/B07ZZ2K7WP>`_ (Target Tracking)

  * The V1 is strongly preferred over the V2 due to the V2 having undesirable FOV choices

* `Pi Camera Module V2 <https://www.amazon.com/Official-Raspberry-Pi-8-megapixel-XYGStudy/dp/B01G01JJJ0>`_ (Target Tracking)

* `Microsoft LifeCam HD-3000 <https://www.andymark.com/products/microsoft-lifecam-hd-3000-camera>`_ (Target Tracking)

* `720p ELP Camera <https://www.amazon.com/SVPRO-Camera-Module-100degree-Distortion/dp/B07C1KYBYC>`_ (Target Tracking)

* `720p Fisheye ELP Camera <https://www.amazon.com/ELP-Camera-170degree-Megapixel-Security/dp/B00VTINRMK/>`_ (Driver Camera)

.. note:: If you test a camera and find that it works with PhotonVision, we encourage you to submit that camera to the performance matrix below.

.. warning::

    The following cameras are known to not work:

    * Most Logitech cameras (specifically the Logitech C270 HD Webcam (PN: 960-000694)) will not work with PhotonVision.

    * The PS3Eye needs a workaround to be usable, for more information see :ref:`our Known Issues page <docs/other/known-issues:Hardware Issues>`

    * Most laptop integrated webcams

Supported Coprocessors
----------------------
* Raspberry Pi 3 / 4, with the newest variants of each being preferred (3B+ and B, respectively).
* Raspberry Pi 3 is preferred **for retroreflective tracking** over 4 due to the GPU acceleration avaliable, more technical information available `here. <https://www.chiefdelphi.com/t/announcing-gloworm-an-inexpensive-and-open-source-vision-module/386370/61?u=pietroglyph>`_
* Raspberry Pi 4 is preferred for **AprilTag tracking** due to better hardware and future GPU acceleration.
* Mini PCs have been testing and show better performance than a Raspberry Pi but require extra effort to wire to the robot / get set up. More information can be found in the set up guide here (HYPERLINK GOES HERE).
* Other coprocessors can be used but may require some extra work / command line usage in order to get it working properly


Performance Matrix
------------------

.. raw:: html

    <embed>

        <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTojOew2d2NQY4PRA98vjkS1ECZ2YNvods-aOdk2x-Q4aF_7r4mcwlyTe8GjUKmUxEiVgGNnJNhEdyd/pubhtml?gid=1779881081&amp;single=true&amp;widget=true&amp;headers=false" width="760" height="500" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>

    </embed>

Please submit performance data to be added to the matrix here:

.. raw:: html

    <embed>

        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSf5iK3pX0Tn8bxpRYgcTAy4scUu14rUvJqkTyfzoKc-GiV7Vg/viewform?embedded=true" width="760" height="500" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>

    </embed>


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
         * Raspberry Pi 3 and Raspberry Pi 4 with the official Pi image with the Pi Cam or CSCore compatible USB Cameras
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
