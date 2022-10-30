Wiring 
======


Off-Robot Wiring
----------------

After imaging your coprocessor, run an ethernet cable from your coprocessor to your computer and power on your coprocessor by plugging it into the wall. 


On-Robot Wiring
---------------

.. note:: We reccomend users use the `SnakeEyes Pi Hat <https://www.playingwithfusion.com/productview.php?pdid=133>`_ as it provides passive power over ethernet (POE) and other useful features to simplify wiring and make your life easier.

Reccomended: Coprocessor with Passive POE (Gloworm, Pi with SnakeEyes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1. Plug the `passive POE injector <https://www.revrobotics.com/rev-11-1210/>`_ into the coprocessor and wire it to PDP/PDB (NOT the VRM).

2. Add a breaker to relevant slot in your PDP/PDB

3. Run an ethernet cable from the passive POE injector to your network switch / radio (we *STRONGLY* reccomend the usage of a network switch, see the networking section for more info.)

Coprocessor without Passive POE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1a. Option 1: Get a micro USB (may be USB-C if using a newer Pi) to USB-A cable and plug the USB A side into a regulator like `this <https://www.amazon.com/KNACRO-Voltage-Regulator-Converter-Module/dp/B01HM12N2C>`_. Then, wire the regulator into your PDP/PDB and the Micro USB / USB C into your pi.

1b. Option 2: Use a USB powerbank to power your Pi. There are rules that regulate the usage of powerbanks so ensure that you aren't breaking them, more information can be found `here <https://www.chiefdelphi.com/t/limelight-powered-by-external-battery/390710>`_.

2. Run an ethernet cable from your Pi to your network switch / radio (we *STRONGLY* reccomend the usage of a network switch, see the networking section for more info.)


------------------------------------------------------------

Once you have wired your coprocessor, you are now ready to install PhotonVision. 