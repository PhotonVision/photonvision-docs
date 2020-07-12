Creating a PhotonCamera
=======================

What is a PhotonCamera?
-----------------------
``PhotonCamera`` is a class in PhotonLib that allows a user to interact with one camera that is connected to hardware that is running Photon Vision. Through this class, users can retrieve yaw, pitch, roll, robot-relative pose, latency, and a wealth of other information.

Constructing a PhotonCamera
---------------------------
The ``PhotonCamera`` class has two constructors: one that takes a ``NetworkTable`` and another that takes in the name of the network table that PhotonVision is broadcasting information over. For ease of use, it is recommended to use the latter.

.. note:: To determine the name of the network table that PhotonVision is broadcasting information over, please see the Settings tab in the PhotonVision UI. The default network table name is ``photonvision``.

.. tabs::
   .. code-tab:: java

      // Creates a new PhotonCamera.
      PhotonCamera camera = new PhotonCamera("photonvision");

   .. code-tab:: c++

      #include <photonlib/lib/PhotonCamera.h>

      // Creates a new PhotonCamera.
      photonlib::PhotonCamera camera{"photonvision"};


Checking for Existence of Targets
---------------------------------
``PhotonCamera`` has a ``hasTargets()/HasTargets()`` method (Java and C++ respectively) that users can utilize to check if their vision system is detecting any targets.

.. tabs::
   .. code-tab:: java

      // Check if there are any targets.
      boolean targets = camera.hasTargets();

   .. code-tab:: c++

      // Check if there are any targets.
      bool targets = camera.HasTargets();

Getting Yaw, Pitch, and Area
----------------------------
``PhotonCamera`` contains three convenience methods for retrieving the yaw, pitch, and area of the best target. These methods are ``getFirstTargetYaw()``/``GetFirstTargetYaw()``, ``getFirstTargetPitch()``/``GetFirstTargetPitch()``, and ``getBestTargetArea()``/``GetBestTargetArea()`` for Java and C++ respectively.

.. tabs::
   .. code-tab:: java

      // Get the yaw, pitch, and area from the camera.
      double yaw = camera.getFirstTargetYaw();
      double pitch = camera.getFirstTargetPitch();
      double area = camera.getFirstTargetArea();

   .. code-tab:: c++

      // Get the yaw, pitch, and area from the camera.
      double yaw = camera.GetFirstTargetYaw();
      double pitch = camera.GetFirstTargetPitch();
      double area = camera.GetBestTargetArea();

.. note:: The units for yaw and pitch are degrees and use standard computer vision directionality. Therefore, a negative yaw means that the recognized target is to the left of the center of the screen and a negative pitch means that the recognized target is below the center of the screen.

Getting the Pipeline Result (Advanced)
--------------------------------------
One can also use the ``getLastResult()``/``GetLastResult()`` (Java and C++ respectively) to obtain the latest :ref:`pipeline result <docs/photonlib/simple-pipeline-result:Simple Pipeline Result>`. An advantage of using this method is that it returns a container with information that is guaranteed to be from the same timestamp. This is important if you are using this data for latency compensation or in an estimator.

.. tabs::
   .. code-tab:: java

      // Get the latest pipeline result.
      SimplePipelineResult result = camera.getLastResult();

   .. code-tab:: c++

      // Get the latest pipeline result.
      photonlib::SimplePipelineResult result = camera.GetLastResult();

.. note:: Unlike other vision software solutions, using the latest result guarantees that all information is from the same timestamp. This is achieveable because the PhotonVision backend sends a byte-packed string of data which is then deserialized by PhotonLib to get target data. For more information, check out the `PhotonLib source code <https://github.com/PhotonVision/photonlib>`_.
