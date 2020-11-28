Creating a PhotonCamera
=======================

What is a PhotonCamera?
-----------------------
``PhotonCamera`` is a class in PhotonLib that allows a user to interact with one camera that is connected to hardware that is running Photon Vision. Through this class, users can retrieve yaw, pitch, roll, robot-relative pose, latency, and a wealth of other information.

Constructing a PhotonCamera
---------------------------
The ``PhotonCamera`` class has two constructors: one that takes a ``NetworkTable`` and another that takes in the name of the network table that PhotonVision is broadcasting information over. For ease of use, it is recommended to use the latter. The name of the NetworkTable (for the string constructor) should be the same as the camera's nickname (from the PhotonVision UI).

.. tabs::
   .. code-tab:: java

      // Creates a new PhotonCamera.
      PhotonCamera camera = new PhotonCamera("MyCamera");

   .. code-tab:: c++

      #include <photonlib/lib/PhotonCamera.h>

      // Creates a new PhotonCamera.
      photonlib::PhotonCamera camera{"MyCamera"};


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
``PhotonCamera`` contains three convenience methods for retrieving the yaw, pitch, and area of the best target. These methods are ``getBestTargetYaw()``/``GetBestTargetYaw()``, ``getBestTargetPitch()``/``GetBestTargetPitch()``, and ``getBestTargetArea()``/``GetBestTargetArea()`` for Java and C++ respectively.

.. tabs::
   .. code-tab:: java

      // Get the yaw, pitch, and area from the camera.
      double yaw = camera.getBestTargetYaw();
      double pitch = camera.getBestTargetPitch();
      double area = camera.getBestTargetArea();

   .. code-tab:: c++

      // Get the yaw, pitch, and area from the camera.
      double yaw = camera.GetBestTargetYaw();
      double pitch = camera.GetBestTargetPitch();
      double area = camera.GetBestTargetArea();

.. note:: The units for yaw and pitch are degrees and use standard computer vision directionality. Therefore, a negative yaw means that the recognized target is to the left of the center of the screen and a negative pitch means that the recognized target is below the center of the screen. Furthermore, area is scaled from 0-100, representing the percentage of the screen taken up by the bounding box.

Saving Pictures to File
-----------------------
A ``PhotonCamera`` can save still images from the input or output video streams to file. This is useful for debugging what a camera is seeing while on the field and confirming targets are being identified properly.

Images are stored within the photonvision configuration directory. Running the "Export" operation in the settings tab will download a .zip file which contains the image captures.

.. tabs::
   .. code-tab:: java

      // Capture pre-process camera stream image
      // TODO
      camera.

      // Capture post-process camera stream image
      // TODO
      camera.

   .. code-tab:: c++

      // Capture pre-process camera stream image
      // TODO
      camera.

      // Capture post-process camera stream image
      // TODO
      camera.


.. note:: Saving images to file takes a bit of time and uses up disk space, so doing it frequently is not recommended. In general, the camera will save an image every 500ms. Calling these methods faster will not result in additional images. Consider tying it to a button press on the driver controller, or the start of an autonomous routine.


Getting the Pipeline Result (Advanced)
--------------------------------------
One can also use the ``getLatestResult()``/``GetLatestResult()`` (Java and C++ respectively) to obtain the latest :ref:`pipeline result <docs/programming/photonlib/simple-pipeline-result:Photon Pipeline Result>`. An advantage of using this method is that it returns a container with information that is guaranteed to be from the same timestamp. This is important if you are using this data for latency compensation or in an estimator.

.. tabs::
   .. code-tab:: java

      // Get the latest pipeline result.
      PhotonPipelineResult result = camera.getLatestResult();

   .. code-tab:: c++

      // Get the latest pipeline result.
      photonlib::PhotonPipelineResult result = camera.GetLatestResult();

.. note:: Unlike other vision software solutions, using the latest result guarantees that all information is from the same timestamp. This is achieveable because the PhotonVision backend sends a byte-packed string of data which is then deserialized by PhotonLib to get target data. For more information, check out the `PhotonLib source code <https://github.com/PhotonVision/photonlib>`_.
