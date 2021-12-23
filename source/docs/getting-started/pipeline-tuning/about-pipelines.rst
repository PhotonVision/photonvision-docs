About Pipelines
===============

What is a pipeline?
^^^^^^^^^^^^^^^^^^^

A vision pipeline represents a series of steps that are used to acquire an image, process it, and analyzing it to find a target. In most FRC games, this means processing an image in order to detect a piece of retroreflective tape. 

Pipelines in PhotonVision, regardless of type, have 4 steps (represented as 4 tabs):

1. Input: This tab allows the raw camera image to be modified before it gets processed. Here, you can set exposure, brightness, gain, orientation, and resolution.

2. Threshold: This tabs allows you to filter our specific colors/pixels in your camera stream through HSV tuning. The end goal here is having a black and white image that will only have your target lit up. 

3. Contours: After thresholding, there will be various contours of your desired target on the screen. The available filters will change based on different pipeline types. Regardless of type, you can filter how the targets are grouped, their intersection, and how the targets are sorted.

4. Output: Now that you have filtered all of your contours, this allows you to manipulate the detected target via orientation, the offset point, and offset.

Types of Pipelines
^^^^^^^^^^^^^^^^^^

Reflective
----------

This is the most common pipeline type and it is based on detecting targets with retroreflective tape. In the contours tab of this pipeline type, you can filter the area, width/height ratio, fullness, degree of speckle rejection.


Colored Shape
-------------

This pipeline type is based on detecting different shapes like circles, triangles, quadrilaterals, or a polygon. An example usage would be detecting yellow PowerCells from the 2020 FRC game. You can read more about the specific settings available in the contours page.
