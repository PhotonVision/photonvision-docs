Known Issues
============

Hardware Issues
---------------

PS3Eye
^^^^^^
Due to an issue with Linux kernels, the drivers for the PS3Eye are no longer supported. If you would still like to use the PS3Eye, you can downgrade your kernel with the following command: ``sudo CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt rpi-update 866751bfd023e72bd96a8225cf567e03c334ecc4``. Note: You must be connected to the internet to run the command.

Software Issues
---------------

LED Control
^^^^^^^^^^^

The logic for controlling LED mode when `multiple cameras are connected` is not fully fleshed out.

For now, if you are using multiple cameras, it is recommended that teams set the value of the NetworkTables entry :code:`photonvision/ledMode` from the robot code to control LED state.
