Orange Pi Installation
======================

Downloading Linux Image
-----------------------

Starting in 2024, PhotonVision provides pre-configured system images for Orange Pi 5 devices.  Download the latest release of the PhotonVision Orange Pi 5 image (.xz file suffixed with ``orangepi5.xz``) from the `releases page <https://github.com/PhotonVision/photonvision/releases>`_. You do not need to extract the downloaded archive file. This image is configured with a ``pi`` user with password ``raspberry``.

For an Orange Pi 4, download the latest release of the Armbian Bullseye CLI image from `here <https://armbian.tnahosting.net/archive/orangepi4/archive/Armbian_23.02.2_Orangepi4_bullseye_current_5.15.93.img.xz>`_.

Flashing the Pi Image
---------------------
An 8GB or larger SD card is recommended.

Use `Balena Etcher <https://www.balena.io/etcher/>`_ to flash an image onto a Orange Pi. Select the downloaded image file, select your microSD card, and flash.

For more detailed instructions on using Etcher, please see the `Etcher website <https://www.balena.io/etcher/>`_.

.. warning:: Using an older version of Balena Etcher may cause bootlooping (the system will repeatedly boot and restart) when imaging your Orange Pi. Updating to the latest Balena Etcher will fix this issue.

.. note:: If you are working on Linux, "dd" can be used in the command line to flash an image.

If you're using an Orange Pi 5, that's it! Orange Pi 4 users will need to install PhotonVision (see below).

Initial User Setup (Orange Pi 4 Only)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Insert the flashed microSD card into your Orange Pi and boot it up. The first boot may take a few minutes as the Pi expands the filesystem. Be sure not to unplug during this process.

Plug your Orange Pi into a display via HDMI and plug in a keyboard via USB once its powered up. For an Orange Pi 4, complete the initial set up which involves creating a root password and adding a user, as well as setting localization language. Additionally, choose “bash” when prompted.

Installing PhotonVision (Orange Pi 4 Only)
------------------------------------------
From here, you can follow :ref:`this guide <docs/installation/sw_install/other-coprocessors:Installing Photonvision>`.

.. note:: You may also want to read the note about big.LITTLE architecture in the :ref:`advanced command line documentation <docs/getting-started/installation/sw_install/advanced-cmd:Advanced Command Line Usage>`.
