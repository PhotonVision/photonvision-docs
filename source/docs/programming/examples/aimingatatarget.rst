Aiming at a Target
==================

Knowledge and Equipment Needed
------------------------------

- Robot with a vision system running PhotonVision
- Target
- Ability to track a target by properly tuning a pipeline

Code
-------

Now that you have properly set up your vision system and have tuned a pipeline, you can now aim your robot/turret at the target using the data from PhotonVision. This data is reported over NetworkTables and includes: latency, whether there is a target detected or not, pitch, yaw, area, skew, and target pose relative to the robot. This data will be used/manipulated by our vendor dependency, PhotonLib. The documentation for the Network Tables API can be found :ref:`here <docs/programming/nt-api/nt-api:Getting Target Information>` and the documentation for PhotonLib :ref:`here <docs/programming/photonlib/adding-vendordep:What is PhotonLib?>`. For right now, all we will be using is yaw. In this example, while the operator holds a button down, the robot will turn towards the goal using the P term of a PID loop. To learn more about how PID loops work, how WPILib implements them, and more, visit  `Advanced Controls (PID) <https://docs.wpilib.org/en/stable/docs/software/advanced-control/introduction/index.html>`_ and `PID Control in WPILib <https://docs.wpilib.org/en/stable/docs/software/advanced-control/controllers/pidcontroller.html#pid-control-in-wpilib>`_.

The following example is from the PhotonLib example repository (`Java <https://github.com/Photo1nVision/photonlib-examples/tree/main/java/aiming-at-target>`_/`C++ <https://github.com/PhotonVision/photonlib-examples/tree/main/cpp/aiming-at-target>`_).

.. tabs::

  .. group-tab:: Java

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonlib-examples/main/java/aiming-at-target/src/main/java/frc/robot/Robot.java
      :language: java
      :linenos:

  .. group-tab:: C++ (Header)

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonlib-examples/main/cpp/aiming-at-target/src/main/include/Robot.h
      :language: c++
      :linenos:

  .. group-tab:: C++ (Source)

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonlib-examples/main/cpp/aiming-at-target/src/main/cpp/Robot.cpp
      :language: c++
      :linenos: