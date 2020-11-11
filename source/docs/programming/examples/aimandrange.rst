Combining Aiming and Getting in Range
=====================================

Knowledge and Equipment Needed
-----------------------------------------------

- Everything required in :ref:`Aiming at a Target <docs/programming/examples/aimingatatarget:Knowledge and Equipment Needed>` and :ref:`Getting in Range of the Target <docs/programming/examples/gettinginrangeofthetarget:Knowledge and Equipment Needed>`.

Code
-------

Now that you know how to both aim and get in range of the target, it is time to combine them both at the same time. This example will take the previous two code examples and make them into one function using the same tools as before. With this example, you now have all the knowledge you need to use PhotonVision on your robot in any game.

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
         final double LINEAR_P = 0.1;
         final double LINEAR_D = 0.0;
         PIDController forwardController = new PIDController(LINEAR_P, 0, LINEAR_D);

         final double ANGULAR_P = 0.1;
         final double ANGULAR_D = 0.0;
         PIDController turnController = new PIDController(ANGULAR_P, 0, ANGULAR_D);

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
            double rotationSpeed;

            if(xboxController.getAButton()) {
                  // Vision-alignment mode
                  // Query the latest result from PhotonVision
                  var result = camera.getLatestResult();

                  if(result.hasTargets()) {
                     // First calculate range
                     double range = PhotonUtils.calculateDistanceToTargetMeters(CAMERA_HEIGHT_METERS,
                        TARGET_HEIGHT_METERS, CAMERA_PITCH_RADIANS, result.getBestTarget().getPitch());

                     // Use this range as the measurement we give to the PID controller.
                     forwardSpeed = forwardController.calculate(range, GOAL_RANGE_METERS);

                     // Also calculate angular power
                     rotationSpeed = turnController.calculate(result.getBestTarget().getYaw(), 0);
                  } else {
                     // If we have no targets, stay still.
                     forwardSpeed = 0;
                     rotationSpeed = 0;
                  }
            } else {
                  //Manual Driver Mode
                  forwardSpeed = xboxController.getY(GenericHID.Hand.kRight);
                  rotationSpeed = xboxController.getX(GenericHID.Hand.kLeft);
            }

            // Use our forward/turn speeds to control the drivetrain
            drive.arcadeDrive(forwardSpeed, rotationSpeed);
         }
      }

   .. code-tab:: c++

      // TODO: Add code
