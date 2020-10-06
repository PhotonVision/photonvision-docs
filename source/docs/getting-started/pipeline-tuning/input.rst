Input
=====

PhotonVision's "Input" tab contains settings that affect the image captured by the currently selected camera. This includes camera exposure and brightness, as well as resolution and orientation.

Resolution
----------

Resolution changes the resolution of the image captured. While higher resolutions are often more accurate than lower resolutions, they also run at a slower update rate.

Exposure and brightness
-----------------------

Camera exposure and brightness control how bright the captured image will be, although they function differently. Camera exposure changes how long the camera shutter lets in light, which changes the overall brightness of the captured image. This is in contrast to brightness, which is a post-processing effect that boosts the overall brightness of the image at the cost of desaturating colors (making colors look less distinct). In general, exposure time should be set as low as possible while still allowing the target to be reliably tracked. In some cases (such as on the Lifecam HD-3000), decreasing exposure can actually increase camera FPS.

After adjusting exposure and brightness, the target should be lit green (or the color of the vision tracking LEDs used, while not being washed out or overblown. The more distinct the color of the target, the more likely it will be tracked reliably.

Orientation
-----------

Orientation can be used to rotate the image prior to vision processing. This can be useful for cases where the camera is not oriented parallel to the ground. Do note that this operation can in some cases significantly reduce FPS.

Stream Resolution
-----------------

This changes the resolution which is used to stream frames from PhotonVision. This does not change the resolution used to perform vision processing. This is useful to reduce bandwidth consumption on the field. In some high-resolution cases, decreasing stream resolution can increase processing FPS.
