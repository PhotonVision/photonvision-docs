Controlling LEDs (Supported Hardware)
=====================================
You can control the vision LEDs of supported hardware via PhotonLib using the ``setLED()`` method on a ``PhotonCamera`` instance. In Java and C++, an ``LEDMode`` enum class is provided to choose values from. These values include, ``kOff``, ``kOn``, ``kBlink``, and ``kDefault``. ``kDefault`` uses the default LED value from the selected pipeline.

.. tabs::
   .. code-tab:: java

      // Blink the LEDs.
      camera.setLED(LEDMode.kBlink);

   .. code-tab:: c++

      // Blink the LEDs.
      camera.SetLED(photonlib::LEDMode::kBlink);
