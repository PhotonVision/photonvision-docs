Simulation Support in PhotonLib
===============================

What Is Supported?
------------------
PhotonLib supports simulation of a Photon Vision camera and processor moving about a field on a robot.

You can use this to help validate your robot code's behavior in simulation without special wrappers or additional hardware.

Simulation Vision World Model
-----------------------------

Sim-specific classes are provided to model sending one frame of a camera image through PhotonVision. Based on what targets are visible, results are published to NetworkTables.

While processing, the given robot ``Pose2d`` is used to analyze which targets should be in view, and determine where they would have shown up in the camera image.

Targets are considered in view if:

1) Their centroid is within the field of view of the camera.
2) The camera is not in driver mode.
3) The target's in-image pixel size is greater than ``minTargetArea``
4) The distance from the camera to the target is less than ``maxLEDRange``

Only the Raw Bytes network tables object is updated in network tables currently. Actual camera images are not simulated.

Latency of processing is not yet modeled.

.. image:: images/SimArchitecture.svg



Simulated Vision System
-----------------------

A ``SimVisionSystem`` represents the camera, coprocessor, and PhotonVision software moving around on the field.

It requires a number of pieces of configuration to accurately simulate your physical setup. Match them to your configuration in PhotonVision, and to your robot's physical dimensions.

.. tabs::
   .. code-tab:: java

        String camName = "MyCamera";
        double camDiagFOV = 75.0; // degrees
        double camPitch = 0.0;     // degrees
        Transform2d cameraToRobot = new Transform2d(new Translation2d(1.2, 0.0), new Rotation2d()); // meters
        double camHeightOffGround = 0.85; // meters
        double maxLEDRange = 20;          // meters
        int camResolutionWidth = 640;     // pixels
        int camResolutionHeight = 480;    // pixels
        double minTargetArea = 10;        // square pixels

        simVision = new SimVisionSystem(camName,
                                        camDiagFOV,
                                        camPitch,
                                        cameraToRobot,
                                        camHeightOffGround,
                                        maxLEDRange,
                                        camResolutionWidth,
                                        camResolutionHeight,
                                        minTargetArea);

   .. code-tab:: c++

        #include "photonlib/SimVisionSystem.h"

        std::string camName = "MyCamera";
        units::degree_t camDiagFOV (75.0);
        units::degree_t camPitch (0.0);
        frc::Transform2d cameraToRobot (frc::Translation2d(1.2_m, 0.0_m), frc::Rotation2d());
        units::meter_t camHeightOffGround (0.85);
        units::meter_t  maxLEDRange (20);
        int camResolutionWidth = 640;   // pixels
        int camResolutionHeight = 480;  // pixels
        double minTargetArea = 10;      // square pixels

        photonlib::SimVisionSystem simVision(camName,
                                             camDiagFOV,
                                             camPitch,
                                             cameraToRobot,
                                             camHeightOffGround,
                                             maxLEDRange,
                                             camResolutionWidth,
                                             camResolutionHeight,
                                             minTargetArea);


After declaring the system, you should create and add one ``SimVisionTarget`` per target on the field you are attempting to detect.

.. tabs::
   .. code-tab:: java

        var targetPose = new Pose2d(new Translation2d(25,10), new Rotation2d()); // meters
        double targetHeightAboveGround = 2.3; // meters
        double targetWidth = 0.54;           // meters
        double targetHeight = 0.25;          // meters

        var newTgt = new SimVisionTarget(targetPose,
                                         targetHeightAboveGround,
                                         targetWidth,
                                         targetHeight);

        simVision.addSimVisionTarget(newTgt);

   .. code-tab:: c++

        frc::Pose2d targetPose (frc::Translation2d(25_m, 10_m), frc::Rotation2d());
        units::meter_t targetHeightAboveGround (2.3);
        units::meter_t targetWidth (0.54);
        units::meter_t targetHeight (0.25);

        photonlib::SimVisionTarget newTgt (targetPose,
                                           targetHeightAboveGround,
                                           targetWidth,
                                           targetHeight);

        simVision.AddSimVisionTarget(newTgt);

Finally, while running the simulation, process simulated camera frames by providing the robot's pose to the system.

.. tabs::
   .. code-tab:: java

        simVision.processFrame(robotPose);

   .. code-tab:: c++

        simVision.ProcessFrame(robotPose);

This will cause NetworkTables to update properly with targets information, representing any targets that are in view of the robot.

Robot software which uses PhotonLib to interact with a camera running PhotonVision should work the same as though a real camera was hooked up and active.


Raw-Data Approach
-----------------

Advanced users may wish to directly provide target information based on an existing detailed simulation.

A ``SimPhotonCamera`` can be created for this purpose. It provides an interface where the user can supply target data via a list of ``PhotonTrackedTarget`` objects.

.. tabs::
   .. code-tab:: java

        @Override
        public void simulationInit() {
            //  ...
            cam = new SimPhotonCamera("MyCamera");
            //  ...
        }

        @Override
        public void simulationPeriodic() {
            //  ...
            ArrayList<PhotonTrackedTarget> visibleTgtList = new ArrayList<PhotonTrackedTarget>();
            visibleTgtList.add(new PhotonTrackedTarget(yawDegrees, pitchDegrees, area, skew, camToTargetTrans)); // Repeat for each target that you see
            cam.submitProcessedFrame(0.0, visibleTgtList);
            //  ...
        }

   .. code-tab:: c++

        #include "photonlib/SimPhotonCamera.h"

        //  ...

        void Robot::SimulationInit(){
            //  ...
            cam = SimPhotonCamera("MyCamera");
            //  ...
        }

        void Robot::SimulationPeriodic(){
            //  ...
            std::vector<PhotonTrackedTarget> visibleTgtList = {};
            visibleTgtList.push_back(PhotonTrackedTarget(yawAngle, pitchAngle, area, 0.0, camToTargetTrans));
            cam.SubmitProcessedFrame(0_sec, wpi::MutableArrayRef<PhotonTrackedTarget>(visibleTgtList));
            //  ...
        }

Note that while there is less code and configuration required to get basic data into the simulation, this approach will cause the user to need to implement much more code on their end to calculate the relative positions of the robot and target. If you already have this, the raw interface may be helpful. However, if you don't, you'll likely want to be looking at the Simulated Vision System first.
