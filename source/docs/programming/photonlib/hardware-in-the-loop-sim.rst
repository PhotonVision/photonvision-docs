Hardware In The Loop Simulation
===============================

Hardware in the loop simulation is using a physical device, such as a PhotonVision camera, to enhance simulation capabilities.  
This is useful for developing and validating code before the camera is attached to a robot.

The first step is to install PhotonVision on your target device.  Instructions can be found `here <https://docs.photonvision.org/en/latest/docs/getting-started/installation/sw_install/index.html>`_ for all devices.

The next step is to configure PhotonVision for simulation.

.. warning:: Do not leave this toggle on when accessing your device on a full robot.

A small amount of configuration is required on the coprocessor.
From the PhotonVision UI, go to the sidebar and select the Settings option.  Within the settings, turn on "Run NetworkTables Server".

The final step is to configure your code to connect to the NetworkTables server run by your instance of PhotonVision.
The code below shows how to disconnect your simulation from the default NetworkTables server and connect it to the PhotonVision hosted one.

.. tab-set-code::
   .. code-block:: java

      if(RobotBase.isSimulation()) {
         NetworkTableInstance inst = NetworkTableInstance.getDefault();
         inst.stopServer();
         // Change the IP address in the below function to the IP address you use to connect to the PhotonVision UI.
         inst.setServer("photonvision.local");
         inst.startClient4("Robot Simulation");
      }

   .. code-block:: c++

      // Change the IP address to the address of your PhotonVision instance
      // TODO
