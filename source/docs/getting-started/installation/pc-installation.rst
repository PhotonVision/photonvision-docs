PC Installation
===============
It is also possible to install PhotonVision on your personal computer and use your webcam for occasional testing. Note that you will need JDK 11 or higher to be able to run PhotonVision.

.. note:: Due to `cscore <https://github.com/wpilibsuite/allwpilib/tree/master/cscore>`_ restrictions, the PhotonVision server backend cannot run on macOS.

Downloading the Latest Stable Release of PhotonVision
-----------------------------------------------------
You can download the latest stable release of PhotonVision from the `GitHub releases page <https://github.com/PhotonVision/photonvision/releases>`_. Make sure that you are not downloading a release that is marked as "Draft" or "Pre-Release" as these versions are not guaranteed to be stable and may contain massive bugs.

Running PhotonVision
--------------------
To run PhotonVision, open a terminal window of your choice and run the following command:

.. code-block:: none

   $ java -jar /path/to/photonvision/photonvision-xxx.jar --disable-networking

.. note:: The ``--disable-networking`` flag prevents PhotonVision from automatically changing network settings on your computer.

If your computer has a compatible webcam connected, PhotonVision should startup without any error messages. If there are error messages, your webcam isn't supported or another issue has occurred. If it is the latter, please open an issue on the `PhotonVision issues page <https://github.com/PhotonVision/photonvision/issues>`_.

Accessing the PhotonVision Interface
------------------------------------
Once the Java backend is up and running, you can access the main vision interface by navigating to ``localhost:5800`` inside your browser.
