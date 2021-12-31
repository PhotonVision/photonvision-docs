Installing PhotonVision on a Limelight
======================================

The Limelight is a proven, reliable, and easy-to-use smart camera.  However, many of the features of PhotonVision exceed the capabilities of the current Limelight software, so loading the PhotonVision software onto the Limelight hardware gives teams the best of both worlds.  Some of the unique features PhotonVision provides are:

- Multiple Targets that each report their own information.
- Multiple cameras, each of which run an independent pipeline at the same time.
- PhotonLib, which makes it easier to retrieve and do calculations on vision data.
- Up to 2x faster processing at higher resolutions.
- Open Source and constantly improving.

Imaging
-------

Download the hardwareConfig.json file for the version of your Limelight:

- :download:`Limelight Version 2 <files/Limelight2/hardwareConfig.json>`.
- :download:`Limelight Version 2+ <files/Limelight2+/hardwareConfig.json>`.

Save this file. You will need it once PhotonVision is installed. This is **REQUIRED** to get the LEDS working and set the correct camera FOV.

Follow the same process used to `image your Limelight <https://docs.limelightvision.io/en/latest/getting_started.html#imaging>`_ but use the .zip file of the latest `Gloworm image <https://github.com/gloworm-vision/pi-gen/releases>`_ of PhotonVision.  The `Gloworm <https://gloworm.vision/>`_ is a smart camera similar to the Limelight in many ways.

.. warning:: We reccomend that you :ref:`update PhotonVision <docs/getting-started/installation/coprocessor-image:Raspberry Pi Installation>` after you image the Limelight if the Gloworm image is older than the latest stable PhotonVision release.

After installation you should be able to `locate the camera <https://gloworm.vision/docs/quickstart/#finding-gloworm>`_ at: ``http://gloworm.local:5800/``

After connecting you may want to set a static IP address.  This can be done by going to the "Networking" section in the "Settings" page and changing the "Static/DHCP" selector in the center to "Static", then entering your desired IP in the field below the selector.  As listed `here <https://docs.wpilib.org/en/latest/docs/networking/networking-introduction/ip-configurations.html>`_, for a robot, this IP must be ``10.TE.AM.X``. The ``X`` can be variable, but we recommend using ``10.TE.AM.11`` for the first IP Camera.  If you would like to change the gloworm.local to something more intuitive you can modify the hostname.

You will then need to :ref:`import <docs/programming/config/config:Importing and Exporting Settings>` the hardwareConfig.json file you downloaded earlier. Again, this is **REQUIRED** or the LEDS will not work and the target measurements will be incorrect.

Troubleshooting
---------------

To turn the LED lights off or on you need to modify the ``ledMode`` network tables entry or the ``camera.setLED`` of PhotonLib.

To find multiple targets you will need to go to the output tab and click the "Show multiple targets" toggle.
