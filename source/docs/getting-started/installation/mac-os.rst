Mac OS Installation
===================

.. warning:: Due to current `cscore <https://github.com/wpilibsuite/allwpilib/tree/main/cscore>`_ restrictions, the PhotonVision server backend may have issues running macOS.

VERY Limited macOS support is available.

Installing Java
---------------
PhotonVision requires a JDK installed and on the system path. JDK 11 or higher is needed. You may already have this if you have installed WPILib. If not, `download and install it from here <https://adoptopenjdk.net/>`_.

Downloading the Latest Stable Release of PhotonVision
-----------------------------------------------------
Download the latest stable .jar of PhotonVision from the `GitHub releases page <https://github.com/PhotonVision/photonvision/releases>`_.

.. note:: Be sure not to download the .jar file with "-raspi" at the end as that is specifically meant for Raspberry Pi coprocessors.

.. warning:: Be careful to pick the latest stable release. "Draft" or "Pre-Release" versions are not stable and often have bugs.

Running PhotonVision
--------------------
To run PhotonVision, open a terminal window of your choice and run the following command:

.. code-block::

   $ java -jar /path/to/photonvision/photonvision-xxx.jar

.. warning:: Due to current `cscore <https://github.com/wpilibsuite/allwpilib/tree/main/cscore>`_ restrictions, the PhotonVision using test mode is all that is known to work currently.

Accessing the PhotonVision Interface
------------------------------------
Once the Java backend is up and running, you can access the main vision interface by navigating to ``localhost:5800`` inside your browser.

.. warning:: Due to current `cscore <https://github.com/wpilibsuite/allwpilib/tree/main/cscore>`_ restrictions, it is unlikley any streams will open from real webcams.
