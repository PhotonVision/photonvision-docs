Simulating Aiming and Getting in Range
======================================

Knowledge and Equipment Needed
-----------------------------------------------

- Everything required in :ref:`Combining Aiming and Getting in Range <docs/examples/aimandrange:Knowledge and Equipment Needed>`.

Background
----------

Full code may be found in the PhotonLib repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simaimandrange>`_/`C++ <https://github.com/PhotonVision/photonvision/tree/master/photonlib-cpp-examples/src/main/cpp/examples/simaimandrange>`_).

The previous examples show how to run PhotonVision on a real robot, with a physical robot drivetrain moving around and interacting with the software.

This example builds upon that, adding support for simulating robot motion and incorporating that motion into a :code:`SimVisionSystem`. This allows you to test control algorithms on your development computer, without requiring access to a real robot.

.. raw:: html

        <video width="85%" controls>
            <source src="../../../_static/assets/simaimandrange.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

Walkthrough
-----------

First, in the main :code:`Robot` source file, we add support to periodically update a new simulation-specific object. This logic only gets used while running in simulation:

.. tabs::

  .. group-tab:: Java

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simaimandrange/Robot.java
      :language: java
      :lines: 109-123
      :linenos:
      :lineno-start: 109

  .. group-tab:: C++

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/simaimandrange/cpp/Robot.cpp
      :language: c++
      :lines: 64-66
      :linenos:
      :lineno-start: 64

Then, we add in the implementation of our new `DrivetrainSim` class. Please reference the `WPILib documentation on physics simulation <https://docs.wpilib.org/en/stable/docs/software/wpilib-tools/robot-simulation/physics-sim.html>`_.

Simulated Vision support is added with the following steps:

Creating the Simulated Vision System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, we create a new :code:`SimVisionSystem` to represent our camera and coprocessor running PhotonVision.

.. tabs::

  .. group-tab:: Java

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simaimandrange/sim/DrivetrainSim.java
      :language: java
      :lines: 66-88
      :linenos:
      :lineno-start: 66

  .. group-tab:: C++

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/simaimandrange/include/DrivetrainSim.h
      :language: c++
      :lines: 72-92
      :linenos:
      :lineno-start: 72


Next, we create objects to represent the physical location and size of the vision targets we are calibrated to detect. This example models the down-field high goal vision target from the 2020 and 2021 games.

.. tabs::

  .. group-tab:: Java

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simaimandrange/sim/DrivetrainSim.java
      :language: java
      :lines: 89-102
      :linenos:
      :lineno-start: 89

  .. group-tab:: C++

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/simaimandrange/include/DrivetrainSim.h
      :language: c++
      :lines: 94-103
      :linenos:
      :lineno-start: 94

Finally, we add our target to the simulated vision system.

.. tabs::

  .. group-tab:: Java

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simaimandrange/sim/DrivetrainSim.java
      :language: java
      :lines: 107-108
      :linenos:
      :lineno-start: 107

  .. group-tab:: C++

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/simaimandrange/include/DrivetrainSim.h
      :language: c++
      :lines: 41
      :linenos:
      :lineno-start: 41

If you have additional targets you want to detect, you can add them in the same way as the first one.


Updating the Simulated Vision System
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once we have all the properties of our simulated vision system defined, the work to do at runtime becomes very minimal. Simply pass in the robot's pose periodically to the simulated vision system.

.. tabs::

  .. group-tab:: Java

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-java-examples/src/main/java/org/photonlib/examples/simaimandrange/sim/DrivetrainSim.java
      :language: java
      :lines: 131-132
      :linenos:
      :lineno-start: 131

  .. group-tab:: C++

    .. remoteliteralinclude:: https://raw.githubusercontent.com/PhotonVision/photonvision/master/photonlib-cpp-examples/src/main/cpp/examples/simaimandrange/cpp/sim/DrivetrainSim.cpp
      :language: c++
      :lines: 39-40
      :linenos:
      :lineno-start: 39

The rest is done behind the scenes.
