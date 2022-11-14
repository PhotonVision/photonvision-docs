Common Issues / Questions
=========================

This page will grow as needed in order to cover commonly seen issues by teams. If this page doesn't help you and you need further assistance, feel free to :ref:`Contact Us<index:Contact Us>`.

Known Issues
------------
All known issues can be found on our `GitHub page <https://github.com/PhotonVision/photonvision/issues>`_.

PS3Eye
^^^^^^
Due to an issue with Linux kernels, the drivers for the PS3Eye are no longer supported. If you would still like to use the PS3Eye, you can downgrade your kernel with the following command: ``sudo CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt rpi-update 866751bfd023e72bd96a8225cf567e03c334ecc4``. Note: You must be connected to the internet to run the command.

LED Control
^^^^^^^^^^^

The logic for controlling LED mode when `multiple cameras are connected` is not fully fleshed out. In its current state, LED control is only enabled when a Pi Camera Module is not in driver mode—meaning a USB camera on its own is unable to control the LEDs.

For now, if you are using multiple cameras, it is recommended that teams set the value of the NetworkTables entry :code:`photonvision/ledMode` from the robot code to control LED state.

Commonly Seen Issues
--------------------

Networking Issues
^^^^^^^^^^^^^^^^^
Ensure that you have followed :ref:`all the recommendations in the networking section <docs/getting-started/installation/networking:Physical Networking>`.

Camera won't show up
^^^^^^^^^^^^^^^^^^^^
If you are using a Pi camera, contact us using the link above. Pi cameras should work just out of the box, meaning there is a bigger issue.

If you are using a USB camera, it is possible your USB Camera isn't supported  by CSCore and therefore won't work with PhotonVision. See :ref:`supported hardware page for more information <docs/hardware/supportedhardware:Supported Cameras>`.

Camera is consistently returning incorrect values when in 3D mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Read the tips on the :ref:`camera calibration page<docs/getting-started/pipeline-tuning/calibration:Calibration Tips>`, follow the advice there, and redo the calibration.

Not getting data from PhotonLib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Ensure your coprocessor version and PhotonLib version match. This can be checked by the settings tab and examining the .json itself (respectively).

2. Ensure that you have your team number set properly.

Unable to download PhotonLib
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Ensure all of your network firewalls are disabled and you aren't on a school-network.

PhotonVision prompts for login on startup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is normal. You don't need to connect a display to your Raspberry Pi to use PhotonVision, just navigate to the relevant webpage (ex. ``photonvision.local:5800``) in order to see the dashboard.

Raspberry Pi enters into boot looping state when using PhotonVision
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is most commonly seen when your Pi doesn't have adequate power / is being undervolted. Ensure that your power supply is functioning properly.

