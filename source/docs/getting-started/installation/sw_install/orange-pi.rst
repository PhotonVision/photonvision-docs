Orange Pi Installation
======================

Downloading Armbian Bullseye CLI
--------------------------------
Download the latest release of the Armbian Bullseye CLI image from `here <https://redirect.armbian.com/region/NA/orangepi4-lts/Bullseye_current>`_.


Flashing the Pi Image
---------------------
An 8GB or larger SD card is recommended.

Use `Balena Etcher <https://www.balena.io/etcher/>`_ to flash an image onto a Orange Pi. Select the downloaded ``.zip`` file, select your microSD card, and flash.

For more detailed instructions on using Etcher, please see the `Etcher website <https://www.balena.io/etcher/>`_.

.. warning:: Using an older version of Balena Etcher may cause bootlooping (the system will repeatedly boot and restart) when imaging your Raspberry Pi. Updating to the latest Balena Etcher will fix this issue.

Initial Setup
-------------
Insert the flashed microSD card into your Orange Pi and boot it up. The first boot may take a few minutes as the Pi expands the filesystem. Be sure not to unplug during this process.

Plug your Orange Pi into a display via HDMI and plug in a keyboard via USB once its powered up. Complete the initial set up which involves creating a root password and adding a user, as well as setting 
localization language. Additionally, choose “bash” when prompted.

Installing PhotonVision
-----------------------
From here, you can follow :ref:`this guide <docs/getting-started/installation/sw_install/other-coprocessors:Installing Photonvision>`.
