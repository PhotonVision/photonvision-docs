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

      #include <photonlib/PhotonCamera.h>

      // Creates a new PhotonCamera.
      photonlib::PhotonCamera camera{"MyCamera"};

.. warning:: Teams must have unique names for all of their cameras regardless of which coprocessor they are attached to.

Getting the Pipeline Result
---------------------------
Use the ``getLatestResult()``/``GetLatestResult()`` (Java and C++ respectively) to obtain the latest :ref:`pipeline result <docs/programming/photonlib/simple-pipeline-result:Photon Pipeline Result>`. An advantage of using this method is that it returns a container with information that is guaranteed to be from the same timestamp. This is important if you are using this data for latency compensation or in an estimator.

.. tabs::
   .. code-tab:: java

      // Get the latest pipeline result.
      PhotonPipelineResult result = camera.getLatestResult();

   .. code-tab:: c++

      // Get the latest pipeline result.
      photonlib::PhotonPipelineResult result = camera.GetLatestResult();

.. note:: Unlike other vision software solutions, using the latest result guarantees that all information is from the same timestamp. This is achieveable because the PhotonVision backend sends a byte-packed string of data which is then deserialized by PhotonLib to get target data. For more information, check out the `PhotonLib source code <https://github.com/PhotonVision/photonvision/tree/master/photon-lib>`_.

Saving Pictures to File
-----------------------
A ``PhotonCamera`` can save still images from the input or output video streams to file. This is useful for debugging what a camera is seeing while on the field and confirming targets are being identified properly.

Images are stored within the photonvision configuration directory. Running the "Export" operation in the settings tab will download a .zip file which contains the image captures.

.. tabs::
   .. code-tab:: java

      // Capture pre-process camera stream image
      camera.takeInputSnapshot();

      // Capture post-process camera stream image
      camera.takeOutputSnapshot();

   .. code-tab:: c++

      // Capture pre-process camera stream image
      camera.TakeInputSnapshot();

      // Capture post-process camera stream image
      camera.TakeOutputSnapshot();


.. note:: Saving images to file takes a bit of time and uses up disk space, so doing it frequently is not recommended. In general, the camera will save an image every 500ms. Calling these methods faster will not result in additional images. Consider tying image captures to a button press on the driver controller, or an appropriate point in an autonomous routine.



