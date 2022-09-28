Windows PC Installation
=======================
PhotonVision may be run on a Windows Desktop PC for basic testing and evaluation.

Installing Java
---------------
PhotonVision requires a JDK installed and on the system path. JDK 11 or higher is needed. You may already have this if you have fully installed the FRC toolchain. If not, `download and install it from here <https://adoptopenjdk.net/>`_.

Downloading the Latest Stable Release of PhotonVision
-----------------------------------------------------
Download the latest stable release of PhotonVision from the `GitHub releases page <https://github.com/PhotonVision/photonvision/releases>`_.

.. warning:: Be careful to pick the latest stable release. "Draft" or "Pre-Release" versions are not stable and often have bugs. 

Running PhotonVision
--------------------
To run PhotonVision, open a terminal window of your choice and run the following command:

.. code-block::

   > java -jar C:\path\to\photonvision\photonvision-xxx.jar

If your computer has a compatible webcam connected, PhotonVision should startup without any error messages. If there are error messages, your webcam isn't supported or another issue has occurred. If it is the latter, please open an issue on the `PhotonVision issues page <https://github.com/PhotonVision/photonvision/issues>`_.

Accessing the PhotonVision Interface
------------------------------------
Once the Java backend is up and running, you can access the main vision interface by navigating to ``localhost:5800`` inside your browser.
