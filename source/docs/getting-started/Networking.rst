Competition Usage / Networking
==============================


Port Forwarding
^^^^^^^^^^^^^^^

If you would like to access your Ethernet-connected vision device from a computer when tethered to the USB port on the roboRIO, you can use `WPILib's <https://docs.wpilib.org/en/stable/docs/networking/networking-utilities/portforwarding.html>`_ ``PortForwarder``.

.. tabs::

   .. code-tab:: java

         PortForwarder.add(5800, "photonvision.local", 5800);

   .. code-tab:: c++

         wpi::PortForwarder::GetInstance().Add(5800, "wpilibpi.local", 5800);

Camera Stream Ports
^^^^^^^^^^^^^^^^^^^

The camera streams start at they begin at 1181 with two ports for each camera (ex. 1181 and 1182 for camera one, 1183 and 1184 for camera 2, etc.). The easiest way to identify the port of the camera that you want is right clicking the stream you want in the dashboard.
