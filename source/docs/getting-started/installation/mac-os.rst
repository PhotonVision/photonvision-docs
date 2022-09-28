Mac OS Installation
===================
PhotonVision may be run on a non-M1 Mac for basic testing and evaluation.

.. note:: Due to `cscore <https://github.com/wpilibsuite/allwpilib/tree/main/cscore>`_ restrictions, the PhotonVision server backend cannot run on macOS.

Installing Java
---------------
PhotonVision requires a JDK installed and on the system path. JDK 11 or higher is needed. You may already have this if you have fully installed the FRC toolchain. If not, `download and install it from here <https://bell-sw.com/pages/liberica_install_guide-11.0.7/>`_.

Downloading the Latest Stable Release of PhotonVision
-----------------------------------------------------
Download the latest stable release of PhotonVision from the `GitHub releases page <https://github.com/PhotonVision/photonvision/releases>`_.

Running PhotonVision
--------------------
To run PhotonVision, open a terminal window of your choice and run the following command:

.. code-block::

   $ java -jar /path/to/photonvision/photonvision-xxx.jar --disable-networking

.. note:: The ``--disable-networking`` flag prevents PhotonVision from automatically changing network settings on your computer.

If your computer has a compatible webcam connected, PhotonVision should startup without any error messages. If there are error messages, your webcam isn't supported or another issue has occurred. If it is the latter, please open an issue on the `PhotonVision issues page <https://github.com/PhotonVision/photonvision/issues>`_.

Accessing the PhotonVision Interface
------------------------------------
Once the Java backend is up and running, you can access the main vision interface by navigating to ``localhost:5800`` inside your browser.
