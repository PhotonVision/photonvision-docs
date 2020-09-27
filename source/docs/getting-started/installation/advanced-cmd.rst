Advanced Command Line Usage
===========================
This article will go over some advanced command line usage that will help you configure PhotonVision on a Linux coprocessor such as the Raspberry Pi. For ease of use, it is highly recommended to use the :ref:`Pi image or install script <docs/getting-started/installation/coprocessor-image:Installing PhotonVision>`.

Running a JAR File
------------------
Assuming ``java`` has been installed, and the appropriate environment variables have been set upon installation (a package manager like ``apt`` should automatically set these), you can use ``java -jar`` to run a JAR file. If you downloaded the latest stable JAR of PhotonVision from the `GitHub releases page <https://github.com/PhotonVision/photonvision/releases>`_, you can run the following to start the program:

.. code-block:: bash

    java -jar /path/to/photonvision/photonvision.jar


Creating a ``systemd`` Service
------------------------------
You can also create a systemd service that will automatically run on startup. To do so, first navigate to ``/lib/systemd/system``. Create a file called ``photonvision.service`` (or name it whatever you want) using ``touch photonvision.service``. Then open this file in the editor of your choice and paste the following text:

.. code-block:: none

    [Unit]
    Description=Service that runs PhotonVision

    [Service]
    WorkingDirectory=/path/to/photonvision
    ExecStart=/usr/bin/java -jar /path/to/photonvision/photonvision.jar

    [Install]
    WantedBy=multi-user.target

Then copy the ``.service`` file to ``/etc/systemd/system/`` using ``cp photonvision.service /etc/systemd/system/photonvision.service``. Then modify the file to have ``644`` permissions using ``chmod 644 /etc/systemd/system/photonvision.service``.

Installing the ``systemd`` Service
----------------------------------
To install the service, simply run ``systemctl enable photonvision.service``.

.. note:: It is recommended to reload configurations by running ``systemctl daemon-reload``.
