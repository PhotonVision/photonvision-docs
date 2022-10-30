Other Debian-Based Co-Processor Installation
============================================

.. warning:: Working with unsupported coprocessors requires some level of "know how" of your target system. The install script has only been tested on Debian/Raspberry Pi OS Buster and Ubuntu Bionic. If any issues arise with your specific OS, please open an issue on our `issues page <https://github.com/PhotonVision/photonvision/issues>`_.

.. note:: We'd love to have your input! If you get PhotonVision working on another coprocessor, consider documenting your steps and submitting a `docs issue <https://github.com/PhotonVision/photonvision-docs/issues>`_., `pull request <https://github.com/PhotonVision/photonvision-docs/pulls>`_ , or `ping us on Discord <https://discord.com/invite/wYxTwym>`_. For example, Limelight and Romi install instructions came about because someone spent the time to figure it out, and did a writeup.

We provide an `install script <https://git.io/JJrEP>`_ for other Debian-based systems (with ``apt``) that will automatically install PhotonVision and make sure that it runs on startup.

.. code-block:: bash

   $ wget https://git.io/JJrEP -O install.sh
   $ sudo chmod +x install.sh
   $ sudo ./install.sh
   $ sudo reboot now

.. note:: Your co-processor will require an Internet connection for this process to work correctly.

For installation on any other co-processors, we recommend reading the :ref:`advanced command line documentation <docs/getting-started/installation/install/advanced-cmd:Advanced Command Line Usage>`.

Updating PhotonVision
---------------------

PhotonVision can be updated by stopping the service, copying in the updated jar, and restarting the service.

For example, from another Linux computer, run the following:

.. code-block:: bash

   $ scp [jar name].jar pi@photonvision.local:~/
   $ ssh pi@photonvision.local
   $ sudo systemctl stop photonvision.service
   $ sudo mv [jar name].jar /opt/photonvision/photonvision.jar
   $ sudo systemctl start photonvision.service
