Installing PhotonVision
=======================
Because we support several co-processors, there are many ways that you can install PhotonVision, based on the co-processor that you are using. For teams using a Raspberry Pi, we have created a Pi image that you can flash. For teams other co-processors such as Nvidia Jetson, we have an install shell script that you can run.

Raspberry Pi Installation
-------------------------
Because we anticipate that most teams will use a Raspberry Pi as their co-processor, we have created a Pi image that users can flash onto their Raspberry Pi that contains the latest version of PhotonVision along with the setup necessary to automatically start PhotonVision on startup.

Downloading the Pi Image
^^^^^^^^^^^^^^^^^^^^^^^^
Download the latest release of the PhotonVision Pi image from the `releases page <https://github.com/PhotonVision/photonvision/releases>`_ to the location of your choice. You do not need to extract the downloaded ZIP file.

.. note:: If using a `Gloworm <https://gloworm.vision/>`_, or a `SnakeEyes Hat <https://www.playingwithfusion.com/productview.php?pdid=133>`_, you will need to use the image found :ref:`here. <docs/hardware/supportedhardware:vendors>`

.. note:: If using you will need to use the image found :ref:`here. <docs/hardware/supportedhardware:vendors>`

Flashing the Pi Image
^^^^^^^^^^^^^^^^^^^^^
It is recommended to use `Balena Etcher <https://www.balena.io/etcher/>`_ to flash an image onto a Raspberry Pi. Simply select the downloaded ``.zip`` file, select your microSD card (we recommend an SD card with a capacity of 8 GB or higher), and flash. For more detailed instructions on using Etcher, please see the `Etcher website <https://www.balena.io/etcher/>`_.

Final Steps
^^^^^^^^^^^
Simply insert the flashed microSD card into your Raspberry Pi and boot it up. After the initial setup process, your Raspberry Pi should be configured for PhotonVision. You can verify this by making sure your Raspberry Pi and computer are connected to the same network and navigating to ``photonvision.local:5800`` in your browser on your computer.

.. note:: If using a `Gloworm <https://gloworm.vision/>`_, you will need to navigate to ``gloworm.local:5800``.

Troubleshooting/Setting a Static IP
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If ``photonvision.local:5800`` or ``gloworm.local:5800`` do not resolve, your mDNS is not set up correctly. To fix this, download `Angry IP Scanner <https://angryip.org/download/#windows>`_ to find PhotonVision/your coprocessor on your network. Once you find it, set the IP to your static IP in PhotonVision. Instructions for that can be found :ref:`here. <docs/hardware/Settings:Networking>` If you continue to have issues, do not hesitate to :ref:`contact us. <index:Contact Us>`

Other Debian-Based Co-Processor Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We provide an `install script <https://git.io/JJrEP>`_ for other Debian-based systems (with ``apt``) that will automatically install PhotonVision and make sure that it runs on startup.

.. code-block:: bash

   $ wget https://git.io/JJrEP -O install.sh
   $ sudo chmod +x install.sh
   $ sudo ./install.sh
   $ sudo reboot now

.. note:: Your co-processor will require an Internet connection for this process to work correctly.

.. note:: The install script has only been tested on Debian/Raspberry Pi OS Buster and Ubuntu Bionic. If any issues arise with your specific OS, please open an issue on our `issues page <https://github.com/PhotonVision/photonvision/issues>`_.

For installation on any other co-processors, we recommend reading the :ref:`advanced command line documentation <docs/getting-started/installation/advanced-cmd:Advanced Command Line Usage>`.

Updating PhotonVision
^^^^^^^^^^^^^^^^^^^^^

In order to update the PhotonVision image, you have three options.

1. Export your settings, reimage your coprocessor using the instructions above, and import your settings back in.

2. Run the following script (if using a Gloworm / Limelight):

.. code-block:: bash

   $ scp [jar name].jar pi@gloworm.local:~/
   $ ssh pi@gloworm.local
   $ sudo systemctl stop photonvision.service
   $ sudo mv [jar name].jar /opt/photonvision/photonvision.jar
   $ sudo systemctl start photonvision.service

3. Download the latest stable .jar from `our releases page <https://github.com/PhotonVision/photonvision/releases>`_, go to the settings tab, and upload the .jar using the Offline Update button.
