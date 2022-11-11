Linux PC Installation
=====================
PhotonVision may be run on a Debian-based Linux Desktop PC for basic testing and evaluation.

Installing Java
---------------
PhotonVision requires a JDK installed and on the system path. JDK 11 is needed (different versions will not work). You may already have this if you have installed WPILib. If not, run the following to install it:

.. code-block::

    $ sudo apt install openjdk-11

.. warning:: Using a JDK other than JDK11 will cause issues when running PhotonVision and is not supported.

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

If your computer has a compatible webcam connected, PhotonVision should startup without any error messages. If there are error messages, your webcam isn't supported or another issue has occurred. If it is the latter, please open an issue on the `PhotonVision issues page <https://github.com/PhotonVision/photonvision/issues>`_.

Accessing the PhotonVision Interface
------------------------------------
Once the Java backend is up and running, you can access the main vision interface by navigating to ``localhost:5800`` inside your browser.
