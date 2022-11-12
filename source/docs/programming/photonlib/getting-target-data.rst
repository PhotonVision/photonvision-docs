Getting Target Data
===================

Constructing a PhotonCamera
---------------------------

What is a PhotonCamera?
^^^^^^^^^^^^^^^^^^^^^^^
``PhotonCamera`` is a class in PhotonLib that allows a user to interact with one camera that is connected to hardware that is running Photon Vision. Through this class, users can retrieve yaw, pitch, roll, robot-relative pose, latency, and a wealth of other information.


The ``PhotonCamera`` class has two constructors: one that takes a ``NetworkTable`` and another that takes in the name of the network table that PhotonVision is broadcasting information over. For ease of use, it is recommended to use the latter. The name of the NetworkTable (for the string constructor) should be the same as the camera's nickname (from the PhotonVision UI).

.. tab-set-code::


     .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/a3bcd3ac4f88acd4665371abc3073bdbe5effea8/photonlib-java-examples/src/main/java/org/photonlib/examples/aimattarget/Robot.java
        :language: java
        :lines: 51-52

     .. rli:: https://github.com/PhotonVision/photonvision/raw/a3bcd3ac4f88acd4665371abc3073bdbe5effea8/photonlib-cpp-examples/src/main/cpp/examples/aimattarget/include/Robot.h
        :language: c++
        :lines: 42-43

.. warning:: Teams must have unique names for all of their cameras regardless of which coprocessor they are attached to.

Getting the Pipeline Result
---------------------------

What is a Photon Pipeline Result?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A ``PhotonPipelineResult`` is a container that contains all information about currently detected targets from a ``PhotonCamera``. You can retrieve the latest pipeline result using the PhotonCamera instance.

Use the ``getLatestResult()``/``GetLatestResult()`` (Java and C++ respectively) to obtain the latest pipeline result. An advantage of using this method is that it returns a container with information that is guaranteed to be from the same timestamp. This is important if you are using this data for latency compensation or in an estimator.

.. tab-set-code::


     .. rli:: https://raw.githubusercontent.com/PhotonVision/photonvision/a3bcd3ac4f88acd4665371abc3073bdbe5effea8/photonlib-java-examples/src/main/java/org/photonlib/examples/aimattarget/Robot.java
        :language: java
        :lines: 79-80

     .. rli:: https://github.com/PhotonVision/photonvision/raw/a3bcd3ac4f88acd4665371abc3073bdbe5effea8/photonlib-cpp-examples/src/main/cpp/examples/aimattarget/cpp/Robot.cpp
         :language: c++
         :lines: 35-36

.. note:: Unlike other vision software solutions, using the latest result guarantees that all information is from the same timestamp. This is achievable because the PhotonVision backend sends a byte-packed string of data which is then deserialized by PhotonLib to get target data. For more information, check out the `PhotonLib source code <https://github.com/PhotonVision/photonvision/tree/master/photon-lib>`_.



Checking for Existence of Targets
---------------------------------
Each pipeline result has a ``hasTargets()``/``HasTargets()`` (Java and C++ respectively) method to inform the user as to whether the result contains any targets.

.. tab-set-code::
   .. code-block:: java

      // Check if the latest result has any targets.
      boolean hasTargets = result.hasTargets();

   .. code-block:: c++

      // Check if the latest result has any targets.
      bool hasTargets = result.HasTargets();

.. warning:: You must *always* check if the result has a target via ``hasTargets()``/``HasTargets()`` before getting targets or else you may get a null pointer exception. Further, you must use the same result in every subsequent call in that loop.

Getting a List of Targets
-------------------------

What is a Photon Tracked Target?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A tracked target contains information about each target from a pipeline result. This information includes yaw, pitch, area, and robot relative pose.


You can get a list of tracked targets using the ``getTargets()``/``GetTargets()`` (Java and C++ respectively) method from a pipeline result.

.. tab-set-code::
   .. code-block:: java

      // Get a list of currently tracked targets.
      List<PhotonTrackedTarget> targets = result.getTargets();

   .. code-block:: c++

      // Get a list of currently tracked targets.
      wpi::ArrayRef<photonlib::PhotonTrackedTarget> targets = result.GetTargets();

Getting the Best Target
-----------------------
You can get the :ref:`best target <docs/getting-started/pipeline-tuning/reflectiveAndShape/contour-filtering:Contour Grouping and Sorting>` using ``getBestTarget()``/``GetBestTarget()`` (Java and C++ respectively) method from the pipeline result.

.. tab-set-code::
   .. code-block:: java

      // Get the current best target.
      PhotonTrackedTarget target = result.getBestTarget();

   .. code-block:: c++

      // Get the current best target.
      photonlib::PhotonTrackedTarget target = result.GetBestTarget();

Getting Target Data
-------------------
You can use the ``getYaw()``/``GetYaw()``, ``getPitch()``/``GetPitch()``, ``getArea()``/``GetArea()``, ``getSkew()``/``GetSkew()``, ``getCorners()``/``GetCorners()``, and ``getCameraToTarget()``/``GetCameraToTarget()`` methods (Java and C++ respectively) within the tracked target class to retrieve the yaw, pitch, area, skew, target corners, and the camera-to-target transform.

.. tab-set-code::
   .. code-block:: java

      // Get information from target.
      double yaw = target.getYaw();
      double pitch = target.getPitch();
      double area = target.getArea();
      double skew = target.getSkew();
      Transform2d pose = target.getCameraToTarget();
      List<TargetCorner> corners = target.getCorners();

   .. code-block:: c++

      // Get information from target.
      double yaw = target.GetYaw();
      double pitch = target.GetPitch();
      double area = target.GetArea();
      double skew = target.GetSkew();
      frc::Transform2d pose = target.GetCameraToTarget();
      wpi::SmallVector<std::pair<double, double>, 4> corners = target.GetCorners();


.. note:: The units for yaw, pitch, and skew are degrees and use standard computer vision directionality. Therefore, a negative yaw means that the recognized target is to the left of the center of the screen, a negative pitch means that the recognized target is below the center of the screen, and skew values are counter-clockwise-positive measured with respect to the horizontal (taking portrait/landscape mode into account). Furthermore, area is scaled from 0-100, representing the percentage of the screen taken up by the bounding box.

.. note:: The camera-to-target transform represents a 2d transformation (translation and rotation) to the target. For more information on how this works, please see the `2d transform documentation <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/geometry/transformations.html#transform2d-and-twist2d>`_.

.. note:: ``getCorners()``/``GetCorners()`` will return the 4 corners of the minimum bounding box rectangle (in no particular order). This is useful for users interested in curve fitting and other more advanced techniques.

Getting the Pipeline Latency
----------------------------
You can also get the pipeline latency from a pipeline result using the ``getLatencyMillis()``/``GetLatency()`` (Java and C++ respectively) methods.

.. tab-set-code::
   .. code-block:: java

      // Get the pipeline latency.
      double latencySeconds = result.getLatencyMillis() / 1000.0;

   .. code-block:: c++

      // Get the pipeline latency.
      units::second_t latency = result.GetLatency();

.. note:: The C++ version of PhotonLib returns the latency in a unit container. For more information on the Units library, see `here <https://docs.wpilib.org/en/stable/docs/software/basic-programming/cpp-units.html>`_.

Saving Pictures to File
-----------------------
A ``PhotonCamera`` can save still images from the input or output video streams to file. This is useful for debugging what a camera is seeing while on the field and confirming targets are being identified properly.

Images are stored within the PhotonVision configuration directory. Running the "Export" operation in the settings tab will download a .zip file which contains the image captures.

.. tab-set-code::

    .. code-block:: java

      // Capture pre-process camera stream image
      camera.takeInputSnapshot();

      // Capture post-process camera stream image
      camera.takeOutputSnapshot();

    .. code-block:: C++

      // Capture pre-process camera stream image
      camera.TakeInputSnapshot();

      // Capture post-process camera stream image
      camera.TakeOutputSnapshot();

.. note:: Saving images to file takes a bit of time and uses up disk space, so doing it frequently is not recommended. In general, the camera will save an image every 500ms. Calling these methods faster will not result in additional images. Consider tying image captures to a button press on the driver controller, or an appropriate point in an autonomous routine.
