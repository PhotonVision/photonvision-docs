AprilTags and RobotPoseEstimator
================================

.. note:: For more information on how to methods to get AprilTag data, look :ref:`here <docs/programming/photonlib/getting-target-data:Getting AprilTag Data From A Target>`.

PhotonLib includes a ``RobotPoseEstimator`` class, which allows you to combine the pose data from all tags in view in order to get one final pose using different strategies.

Creating an ``AprilTagFieldLayout``
-----------------------------------
``AprilTagFieldLayout`` is used to represent a layout of AprilTags within a space (field, shop at home, classroom, etc.). WPILib provides a JSON that describes the layout of AprilTags on the field which you can then use in the AprilTagFieldLayout constructor. You can also specify a custom layout.

The API documentation can be found in here: `Java <https://github.wpilib.org/allwpilib/docs/beta/java/edu/wpi/first/apriltag/AprilTagFieldLayout.html>`_ and `C++ <https://github.wpilib.org/allwpilib/docs/beta/cpp/classfrc_1_1_april_tag_field_layout.html>`_.

.. tab-set-code::
   .. code-block:: java

      // The parameter for loadFromResource() will be different depending on the game.
      AprilTagFieldLayout aprilTagFieldLayout = new ApriltagFieldLayout(AprilTagFieldLayout.loadFromResource(AprilTagFields.k2022RapidReact.m_resourceFile));

   .. code-block:: c++

      // Two example tags in our layout -- ID 0 at (3, 3) and 0 rotation, and
      // id 1 and (5, 5) and 0 rotation.
      std::vector<frc::AprilTag> tags = {
          {0, frc::Pose3d(units::meter_t(3), units::meter_t(3), units::meter_t(3),
                          frc::Rotation3d())},
          {1, frc::Pose3d(units::meter_t(5), units::meter_t(5), units::meter_t(5),
                          frc::Rotation3d())}};
      std::shared_ptr<frc::AprilTagFieldLayout> aprilTags =
          std::make_shared<frc::AprilTagFieldLayout>(tags, 54_ft, 27_ft);

Creating a ``RobotPoseEstimator``
---------------------------------
The RobotPoseEstimator has a constructor that takes an ``AprilTagFieldLayout`` (see above), ``PoseStrategy``, and ``ArrayList<Pair<PhotonCamera, Transform3d>>``. ``PoseStrategy`` has five possible values:

* LOWEST_AMBIGUITY
    * Choose the Pose with the lowest ambiguity
* CLOSEST_TO_CAMERA_HEIGHT
    * Choose the Pose which is closest to the camera height
* CLOSEST_TO_REFERENCE_POSE
    * Choose the Pose which is closest to the camera height
* CLOSEST_TO_LAST_POSE
    * Choose the Pose which is closest to the last pose calculated
* AVERAGE_BEST_TARGETS
    * Choose the Pose which is the average of all the poses from each tag

.. tab-set-code::
   .. code-block:: java

      //Forward Camera
      cam = new PhotonCamera("testCamera");
      Transform3d robotToCam = new Transform3d(new Translation3d(0.5, 0.0, 0.5), new Rotation3d(0,0,0)); //Cam mounted facing forward, half a meter forward of center, half a meter up from center.

      // ... Add other cameras here

      // Assemble the list of cameras & mount locations
      var camList = new ArrayList<Pair<PhotonCamera, Transform3d>>();
      camList.add(new Pair<PhotonCamera, Transform3d>(cam, robotToCam));
      RobotPoseEstimator robotPoseEstimator = new RobotPoseEstimator(aprilTagFieldLayout, PoseStrategy.CLOSEST_TO_REFERENCE_POSE, camList);

   .. code-block:: c++

      // Forward Camera
      std::shared_ptr<photonlib::PhotonCamera> cameraOne =
          std::make_shared<photonlib::PhotonCamera>("testCamera");
      // Camera is mounted facing forward, half a meter forward of center, half a
      // meter up from center.
      frc::Transform3d robotToCam =
          frc::Transform3d(frc::Translation3d(0.5_m, 0_m, 0.5_m),
                          frc::Rotation3d(0_rad, 0_rad, 0_rad));

      // ... Add other cameras here

      // Assemble the list of cameras & mount locations
      std::vector<
          std::pair<std::shared_ptr<photonlib::PhotonCamera>, frc::Transform3d>>
          cameras;
      cameras.push_back(std::make_pair(cameraOne, robotToCam));

      photonlib::RobotPoseEstimator estimator(
          aprilTags, photonlib::CLOSEST_TO_REFERENCE_POSE, cameras);

Using a ``RobotPoseEstimator``
------------------------------
Calling ``update()`` on your ``RobotPoseEstimator`` will return a ``Pair<Pose3d, Double>``, which includes a ``Pose3d`` of the latest estimated pose (using the selected strategy) along with a ``Double`` of the latency in milliseconds. You should be updating your `drivetrain pose estimator <https://docs.wpilib.org/en/latest/docs/software/advanced-controls/state-space/state-space-pose-estimators.html>`_ with the result from the ``RobotPoseEstimator`` every loop using ``addVisionMeasurement()``. See our `code example <https://www.google.com/>`_ for more.

.. tab-set-code::
   .. code-block:: java

        public Pair<Pose2d, Double> getEstimatedGlobalPose(Pose2d prevEstimatedRobotPose) {
            robotPoseEstimator.setReferencePose(prevEstimatedRobotPose);

            double currentTime = Timer.getFPGATimestamp();
            Optional<Pair<Pose3d, Double>> result = robotPoseEstimator.update();
            if (result.isPresent()) {
                return new Pair<Pose2d, Double>(result.get().getFirst().toPose2d(), currentTime - result.get().getSecond());
            } else {
                return new Pair<Pose2d, Double>(null, 0.0);
            }
        }

   .. code-block:: c++

      std::pair<frc::Pose2d, units::millisecond_t> getEstimatedGlobalPose(
          frc::Pose3d prevEstimatedRobotPose) {
        robotPoseEstimator.SetReferencePose(prevEstimatedRobotPose);
        units::millisecond_t currentTime = frc::Timer::GetFPGATimestamp();
        auto result = robotPoseEstimator.Update();
        if (result.second) {
          return std::make_pair<>(result.first.ToPose2d(),
                                  currentTime - result.second);
        } else {
          return std::make_pair(frc::Pose2d(), 0_ms);
        }
      }

Additional ``RobotPoseEstimator`` Methods
-----------------------------------------

``setRefrencePose(Pose3d referencePose)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Updates the stored reference pose when using the CLOSEST_TO_REFERENCE_POSE strategy.

``setLastPose(Pose3d lastPose)``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update the stored last pose. Useful for setting the initial estimate when using the CLOSEST_TO_LAST_POSE strategy.
