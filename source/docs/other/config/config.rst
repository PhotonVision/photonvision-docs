PhotonVision's Configuration Directory
======================================

PhotonVision stores and loads settings in the :code:`photonvision_config` directory, in the same folder as the PhotonVision JAR is stored. On the Pi image as well as the Gloworm, this is in the :code:`/opt/photonvision` directory. The contents of this directory can be exported as a zip archive from the settings page of the interface, under "export settings". These settings can later be uploaded using "import settings", to restore configurations from previous backups. The directory structure is outlined below.

- calibImgs

   - Images saved from the last run of the calibration routine

- cameras

   - Contains a subfolder for each camera. This folder contains the following files:
   - pipelines folder, which contains a :code:`json` file for each user-created pipeline.
   - config.json, which contains all camera-specific configuration. This includes FOV, pitch, current pipeline index, and calibration data
   - drivermode.json, which contains settings for the driver mode pipeline

- imgSaves

   - Contains images saved with the 

- logs
- hardwareSettings.json
- networkSettings.json