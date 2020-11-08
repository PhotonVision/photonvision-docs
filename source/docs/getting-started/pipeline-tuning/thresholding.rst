Thresholding
============

In this step, we want to tune our HSV thresholds such that only the goal color remains after the thresholding. The `HSV color representation <https://en.wikipedia.org/wiki/HSL_and_HSV>`__ is similar to RGB in that it represents colors. However, HSV represents colors with hue, saturation and value components. Hue refers to the color, while saturation and value describe its richness and brightness.

In PhotonVision, HSV thresholds is available in the "Threshold" tab.

.. raw:: html

        <video width="85%" controls>
            <source src="../../../_static/assets/tuningHueSatVal.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>

Color Picker
------------

The color picker can be used to quickly adjust HSV values. "Set to average" will set the HSV range to the color of the pixel selected, while "shrink range" and "expand range" will change the HSV threshold to include or exclude the selected pixel, respectively.

.. raw:: html

        <video width="85%" controls>
            <source src="../../../_static/assets/colorPicker.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
