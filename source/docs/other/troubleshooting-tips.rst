Troubleshooting / Tips
======================

Troubleshooting
---------------

Networking Issues
^^^^^^^^^^^^^^^^^
If you are having networking issues (NetworkTables issues, having issues downloading vendor deps, Romi connection issues w/ PhotonVision, etc.) be sure to check your `firewall settings <https://docs.wpilib.org/en/stable/docs/networking/networking-introduction/windows-firewall-configuration.html>`_. Using School Wi-Fi networks can also cause issues.

Tips
----

Use a Network Switch
^^^^^^^^^^^^^^^^^^^^

Whenever you need to use the second radio ethernet port for something (ex. for a coprocessor, Gloworm, etc.), you need to use a network switch. Historically, the OM5P-AC has had issues when using that second ethernet port which are detailed in `this ChiefDelphi thread. <https://www.chiefdelphi.com/t/raspberry-pi-wiring-do-you-need-a-network-switch/391330>`_  We recommend reading `this whitepaper from FRC Team 900 <https://team900.org/blog/ZebraSwitch/>`_ for network switch recommendations.
