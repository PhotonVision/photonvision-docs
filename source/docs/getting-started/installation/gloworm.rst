Gloworm Installation
====================
While not currently in production, PhotonVision still supports Gloworm vision processing cameras.

Downloading the Gloworm Image
-------------
Download the latest `Gloworm release of PhotonVision <https://github.com/gloworm-vision/pi-img-updator/releases>`_. You do not need to extract the downloaded ZIP file.

Flashing the Gloworm Image
---------------------
Plug a USB C cable from your computer into the USB C port on Gloworm labeled with a download icon.

Use `Balena Etcher <https://www.balena.io/etcher/>`_ to flash an image onto the coprocessor.

Run BalenaEtcher as an administrator. Select the downloaded ``.zip`` file.

Select the compute module. If it doesn't show up after 30s try using another USB port, initialization may take a while. If prompted, install the recommended missing drivers.

Hit flash. Wait for flashing to complete, then disconnect your USB C cable.

Final Steps
-----------
Power your device per its documentation and connect it to a robot network.

You should be able to locate the camera at ``http://gloworm.local:5800/`` in your browser on your computer when connected to the robot.

Troubleshooting/Setting a Static IP
-----------------------------------
If ``http://gloworm.local:5800`` does not resolve, or you do not want to use mDNS, try to connect to the IP address directly.

Download and run `Angry IP Scanner <https://angryip.org/download/#windows>`_ to find PhotonVision/your coprocessor on your network.

Once you find it, set the IP to a desired :ref:`static IP in PhotonVision. <docs/hardware/Settings:Networking>`

Updating PhotonVision
---------------------
Download the latest stable .jar from `the releases page <https://github.com/PhotonVision/photonvision/releases>`_, go to the settings tab, and upload the .jar using the Offline Update button.

As an alternative option - Export your settings, reimage your coprocessor using the instructions above, and import your settings back in.

Hardware Troubleshooting
------------------------
To turn the LED lights off or on you need to modify the ``ledMode`` network tables entry or the ``camera.setLED`` of PhotonLib.


Support Links
-------------

* `Website/Documentation <http://web.archive.org/web/20220525051935/https://gloworm.vision/>`__

* `Image <https://github.com/gloworm-vision/pi-img-updator/releases>`__

* `Discord <https://discord.com/invite/DncQRky>`__
