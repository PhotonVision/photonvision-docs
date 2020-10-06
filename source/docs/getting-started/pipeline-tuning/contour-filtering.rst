Contour Filtering and Grouping
==============================

Contours that make it past thresholding are filtered and grouped so that only likely targets remain.

Filtering Options
-----------------

Contours can be filtered by area, width/height ratio, "fullness", and "speckle rejection" percentage.

Area filtering adjusts the percentage of overall image area that contours are allowed to occupy. The area of valid contours is shown in the "target info" card on the right.

Ratio adjusts the width to height ratio of allowable contours. For example, a width to height filtering range of [2, 3] would allow targets that are 250 x 100 pixels in size through.

Fullness is a measurement of the ratio between the contour's area and the area of its bounding rectangle. This can be used to reject contours that are for example solid blobs.

Finally, speckle rejection is an algorithm that can discard contours whose area are below a certain percentage of the average area of all visible contours. This might be useful in rejecting stray lights or image noise.

Contour Grouping and Sorting
----------------------------

These options change how contours are grouped together and sorted. Target grouping can pair adjacent contours, such as the targets found in 2019. Target intersection defines where the targets would intersect if you extended them infinitely, for example, to only group targets tipped "towards" each other in 2019.

Finally, target sort defines how targets are ranked, from "best" to "worst." The available options are:

- Largest
- Smallest
- Highest (towards the top of the image)
- Lowest
- Rightmost (Best target on the right, worst on left)
- Leftmost
- Centermost
