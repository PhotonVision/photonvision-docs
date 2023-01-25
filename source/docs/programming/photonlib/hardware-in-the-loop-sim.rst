Hardware In The Loop Simulation
===============================

Hardware in the loop simulation is using a physical device, such as a PhotonVision camera, to augment simulation capabilities.  
This is useful for testing the physical capabilities of a camera, without having to run it on a full robot.

The first step is to install PhotonVision on your target device.  Instructions can be found `here <https://docs.photonvision.org/en/latest/docs/getting-started/installation/sw_install/index.html>`_ for all devices.

The next step is to configure PhotonVision for simulation.
.. warning:: Do not leave this toggle on when accessing your device on a full robot.
In the settings GUI, turn on "Run NetworkTables Server".

The final step is to configure your code to connect to the NetworkTables server run by your instance of PhotonVision.
The code below shows how to disconnect your simulation from the default NetworkTables server and connect it to the PhotonVision hosted one.

.. tab-set-code::
   .. code-block:: java

      // Change the IP address to the address of your PhotonVision instance
      if(isSimulation()) {
         NetworkTableInstance inst = NetworkTableInstance.getDefault();
         inst.stopServer();
         inst.setServer("photonvision.local");
         inst.startClient4("Robot Simulation");
      }

   .. code-block:: c++

      // Change the IP address to the address of your PhotonVision instance
      // TODO
