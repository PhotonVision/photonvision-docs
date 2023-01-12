Networking Troubleshooting
==========================

Before reading further, ensure that you follow all the reccomendations in our networking section. You must be following these guidelines in order for PhotonVision to work properly, other networking setups are not officially supported.

photonvision.local Not Found
----------------------------

Use `Angry IP Scanner <https://angryip.org/>`_ and look for an IP that has port 5800 open. Then go to your web browser and do <IP ADDRESS>:5800.

Alternatively, you can plug your coprocessor into a display, plug in a keyboard, and run ``hostname -I`` in the terminal. This should give you the IP Address of your coprocessor, then go to your web browser and do <IP ADDRESS>:5800.

If nothing shows up, ensure your coprocessor has power, and you are following all of our networking reccomendations, feel free to :ref:`contact us <index:contact us>` and we will help you.

Can't Connect To Robot
----------------------

Please check that:
1. You don't have the NetworkTables Server on (toggleable in the settings tab). Turn this off when doing work on a robot.
2. You have your team number set properly in the settings tab.
3. Your camera name in the ``PhotonCamera`` constructor matches the name in the UI.
4. You are using the 2023 version of WPILib and RoboRIO image.
5. Your robot is on.

If all of the above are met and you still have issues, feel free to :ref:`contact us <index:contact us>` and we will help you.
