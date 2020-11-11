Getting in Range of the Target
==============================

Knowledge and Equipment Needed
-----------------------------------------------

- Everything required in :ref:`Aiming at a Target <docs/programming/examples/aimingatatarget:Knowledge and Equipment Needed>`.
- Large space where your robot can move around freely

Code
-------

In FRC, a mechanism usually has to be a certain distance away from it’s target in order to be effective and score. In the last example, we showed how to aim your robot at the target. Now you will learn how to move to a certain distance from the target. In order to properly complete this example, ensure that your robot is pointed towards the target, but this will not be necessary in the future. This example is similar to the previous one and will also be using the P term of the PID loop and PhotonLib, specifically the distance function of PhotonUtils. While the operator holds down a button, the robot will drive towards the target and get in range.

.. warning:: The PhotonLib utility to calculate distance depends on the camera being at a different vertical height than the camera. If this is not the case, a different method for estimating distance, such as target width or area, must be used.

.. tabs::

   .. code-tab:: java

      public class Robot extends TimedRobot {

         // Constants such as camera and target height stored. Change per robot and goal!
         final double CAMERA_HEIGHT_METERS = Units.inchesToMeters(24);
         final double TARGET_HEIGHT_METERS = Units.feetToMeters(5);
         // Angle between horizontal and the camera.
         final double CAMERA_PITCH_RADIANS = Units.degreesToRadians(0);

         // How far from the target we want to be
         final double GOAL_RANGE_METERS = Units.feetToMeters(3);

         // Change this to match the name of your camera
         PhotonCamera camera = new PhotonCamera("photonvision");

         // PID constants should be tuned per robot
         final double P_GAIN = 0.1;
         final double D_GAIN = 0.0;
         PIDController controller = new PIDController(P_GAIN, 0, D_GAIN);

         XboxController xboxController;

         // Drive motors
         PWMVictorSPX leftMotor = new PWMVictorSPX(0);
         PWMVictorSPX rightMotor = new PWMVictorSPX(1);
         DifferentialDrive drive = new DifferentialDrive(leftMotor, rightMotor);

         @Override
         public void robotInit() {
            xboxController = new XboxController(0);
         }

         @Override
         public void teleopPeriodic() {
            double forwardSpeed;
            double rotationSpeed = xboxController.getX(GenericHID.Hand.kLeft);

            if(xboxController.getAButton()) {
                  // Vision-alignment mode
                  // Query the latest result from PhotonVision
                  var result = camera.getLatestResult();

                  if(result.hasTargets()) {
                     // First calculate range
                     double range = PhotonUtils.calculateDistanceToTargetMeters(CAMERA_HEIGHT_METERS,
                        TARGET_HEIGHT_METERS, CAMERA_PITCH_RADIANS, result.getBestTarget().getPitch());

                     // Use this range as the measurement we give to the PID controller.
                     forwardSpeed = controller.calculate(range, GOAL_RANGE_METERS);
                  } else {
                     // If we have no targets, stay still.
                     forwardSpeed = 0;
                  }
            } else {
                  //Manual Driver Mode
                  forwardSpeed = xboxController.getY(GenericHID.Hand.kRight);
            }

            // Use our forward/turn speeds to control the drivetrain
            drive.arcadeDrive(forwardSpeed, rotationSpeed);
         }
      }

   .. code-tab:: c++

      // TODO: Add code
