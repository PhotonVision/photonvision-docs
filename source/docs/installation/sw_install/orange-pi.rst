Orange Pi Installation
======================

Downloading Linux Image
-----------------------
For an Orange Pi 4, download the latest release of the Armbian Bullseye CLI image from `here <https://armbian.tnahosting.net/archive/orangepi4/archive/Armbian_23.02.2_Orangepi4_bullseye_current_5.15.93.img.xz>`_.

For an Orange Pi 5, download the latest release of either Debian Bullseye or Ubuntu Jammy (22.04). For both, you should get the "server" version. You can get the images from the `Orange Pi website <http://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/service-and-support/Orange-pi-5.html>`_.


Flashing the Pi Image
---------------------
An 8GB or larger SD card is recommended.

Use `Balena Etcher <https://www.balena.io/etcher/>`_ to flash an image onto a Orange Pi. Select the downloaded ``.zip`` file, select your microSD card, and flash.

The Orange Pi 5 images from Orange Pi are compressed with 7Zip (extension ".7z"), and you will need to extract the image first.

For more detailed instructions on using Etcher, please see the `Etcher website <https://www.balena.io/etcher/>`_.

.. warning:: Using an older version of Balena Etcher may cause bootlooping (the system will repeatedly boot and restart) when imaging your Orange Pi. Updating to the latest Balena Etcher will fix this issue.

.. note:: If you are working on Linux, "dd" can be used in the command line to flash an image.

Initial Setup
-------------
Insert the flashed microSD card into your Orange Pi and boot it up. The first boot may take a few minutes as the Pi expands the filesystem. Be sure not to unplug during this process.

Plug your Orange Pi into a display via HDMI and plug in a keyboard via USB once its powered up. For an Orange Pi 4, complete the initial set up which involves creating a root password and adding a user, as well as setting localization language. Additionally, choose “bash” when prompted.

Installing PhotonVision
-----------------------
From here, you can follow :ref:`this guide <docs/installation/sw_install/other-coprocessors:Installing Photonvision>`.
