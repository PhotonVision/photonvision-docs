Combining Aiming and Getting in Range
=====================================


The following example is from the PhotonLib example repository (`Java <https://github.com/PhotonVision/photonvision/tree/master/photonlib-java-examples/src/main/java/org/photonlib/examples/aimandrange>`_/`C++ <https://github.com/PhotonVision/photonvision/tree/master/photonlib-cpp-examples/src/main/cpp/examples/aimandrange>`_).

Knowledge and Equipment Needed
-----------------------------------------------

- Everything required in :ref:`Aiming at a Target <docs/examples/aimingatatarget:Knowledge and Equipment Needed>` and :ref:`Getting in Range of the Target <docs/examples/gettinginrangeofthetarget:Knowledge and Equipment Needed>`.

Code
-------

Now that you know how to both aim and get in range of the target, it is time to combine them both at the same time. This example will take the previous two code examples and make them into one function using the same tools as before. With this example, you now have all the knowledge you need to use PhotonVision on your robot in any game.

.. tab-set::

    .. tab-item:: Java

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-java-examples/src/main/java/org/photonlib/examples/aimandrange/Robot.java
         :language: java
         :lines: 42-111
         :linenos:
         :lineno-start: 42

    .. tab-item:: C++ (Header)

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-cpp-examples/src/main/cpp/examples/aimandrange/include/Robot.h
         :language: cpp
         :lines: 27-71
         :linenos:
         :lineno-start: 27

    .. tab-item:: C++ (Source)

       .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/661f8b2c0495474015f6ea9a89d65f9788436a05/photonlib-cpp-examples/src/main/cpp/examples/aimandrange/cpp/Robot.cpp
         :language: cpp
         :lines: 25-67
         :linenos:
         :lineno-start: 25
