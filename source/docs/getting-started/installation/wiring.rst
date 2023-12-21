Wiring
======


Off-Robot Wiring
----------------

Plugging your coprocessor into the wall via a power brick will suffice for off robot wiring.

.. note:: Please make sure your chosen power supply can provide enough power for your coprocessor. Undervolting (where enough power isn't being supplied) can cause many issues.


On-Robot Wiring
---------------

.. note:: We recommend users use the `SnakeEyes Pi Hat <https://www.playingwithfusion.com/productview.php?pdid=133>`_ as it provides passive power over ethernet (POE) and other useful features to simplify wiring and make your life easier.

Recommended: Coprocessor with Passive POE (Gloworm, Pi with SnakeEyes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Plug the `passive POE injector <https://www.revrobotics.com/rev-11-1210/>`_ into the coprocessor and wire it to PDP/PDB (NOT the VRM).

2. Add a breaker to relevant slot in your PDP/PDB

3. Run an ethernet cable from the passive POE injector to your network switch / radio (we *STRONGLY* recommend the usage of a network switch, see the networking section for more info.)

Coprocessor without Passive POE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1a. Option 1: Get a micro USB (may be USB-C if using a newer Pi) to USB-A cable and plug the USB A side into a regulator like `this <https://www.amazon.com/KNACRO-Voltage-Regulator-Converter-Module/dp/B01HM12N2C/ref=sr_1_2>`_. Then, wire the regulator into your PDP/PDB and the Micro USB / USB C into your coprocessor.

1b. Option 2: Use a USB power bank to power your coprocessor. Refer to this year's robot rulebook on legal implementations of this.

1. Run an ethernet cable from your Pi to your network switch / radio (we *STRONGLY* recommend the usage of a network switch, see the networking section for more info.)


------------------------------------------------------------

Once you have wired your coprocessor, you are now ready to install PhotonVision.
