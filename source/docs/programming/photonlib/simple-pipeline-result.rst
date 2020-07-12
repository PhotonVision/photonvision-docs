Simple Pipeline Result
======================

What is a Simple Pipeline Result?
---------------------------------

A ``SimplePipelineResult`` is a container that contains all information about currently detected targets from a ``PhotonCamera``. You can :ref:`retrieve the latest pipeline result <docs/photonlib/creating-photon-camera:Getting the Pipeline Result (Advanced)>` using the ``getLastResult()``/``GetLastResult()`` (Java and C++ respectively) on a ``PhotonCamera`` instance.

Checking for Existence of Targets
---------------------------------
Each pipeline result has a ``hasTargets()``/``HasTargets()`` (Java and C++ respectively) method to inform the user as to whether the result contains any targets.

.. tabs::
   .. code-tab:: java

      // Check if the latest result has any targets.
      boolean hasTargets = result.hasTargets();

   .. code-tab:: c++

      // Check if the latest result has any targets.
      bool hasTargets = result.HasTargets();


Getting a List of Targets
-------------------------
You can get a list of :ref:`simple tracked targets <docs/photonlib/simple-tracked-target:Simple Tracked Target>` using the ``getTargets()``/``GetTargets()`` (Java and C++ respectively) method from a pipeline result.

.. tabs::
   .. code-tab:: java

      // Get a list of currently tracked targets.
      List<SimpleTrackedTarget> targets = result.getTargets();

   .. code-tab:: c++

      // Get a list of currently tracked targets.
      std::vector<photonlib::SimpleTrackedTarget> targets = result.GetTargets();

Getting the Pipeline Latency
----------------------------
You can also get the pipeline latency from a pipeline result using the ``getLatencyMillis()``/``GetLatency()`` (Java and C++ respectively) methods.

.. tabs::
   .. code-tab:: java

      // Get the pipeline latency.
      double latencySeconds = getLatencyMillis() / 1000.0;

   .. code-tab:: c++

      // Get the pipeline latency.
      units::second_t latency = GetLatency();

.. note:: The C++ version of PhotonLib returns the latency in a unit container. For more information on the Units library, see `here <https://docs.wpilib.org/en/stable/docs/software/basic-programming/cpp-units.html>`_.
