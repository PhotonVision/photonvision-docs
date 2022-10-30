Limelight Installation
======================
PhotonVision  supports running on `Limelight <https://limelightvision.io/>`_ FRC vision processing hardware.

Imaging
-------
Limelight imaging is a very similar process to Gloworm, but with extra steps.

Base Install Steps
^^^^^^^^^^^^^^^^^^
Due to the similarities in hardware, follow the :ref:`Gloworm install instructions <docs/getting-started/installation/install/gloworm:Gloworm Installation>`.


Hardware-Specific Steps
^^^^^^^^^^^^^^^^^^^^^^^
Download the hardwareConfig.json file for the version of your Limelight:

- :download:`Limelight Version 2 <files/Limelight2/hardwareConfig.json>`.
- :download:`Limelight Version 2+ <files/Limelight2+/hardwareConfig.json>`.

Save this file. You will need it once PhotonVision is installed. This is **REQUIRED** to get the LEDS working and set the correct camera FOV.

:ref:`Import the hardwareConfig.json file <docs/hardware/config:Importing and Exporting Settings>`. Again, this is **REQUIRED** or target measurements will be incorrect.
