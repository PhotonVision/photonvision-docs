Build Instructions
==================

This section contains the build instructions from the source code available at `our GitHub page <https://github.com/PhotonVision/photonvision>`_.

Development Setup
-----------------

Prerequisites
~~~~~~~~~~~~~

| **Java Development Kit:** This project requires Java Development Kit (JDK) 11 to be compiled. This is the same Java version that comes with WPILib. If you don't have this JDK with WPILib, you can follow the instructions to install JDK 11 for your platform `here <https://bell-sw.com/pages/liberica_install_guide-11.0.7//>`_.
| **Node JS:** The UI is written in Node JS. To compile the UI, Node 10 or newer is required. To install Node JS follow the instructions for your platform `on the official Node JS website <https://nodejs.org/en/download/>`_.

Compiling Instructions
----------------------

Getting the Source Code
~~~~~~~~~~~~~~~~~~~~~~~
Get the source code from git:

.. code-block:: bash

   git clone https://github.com/PhotonVision/photonvision

or alternatively download to source code from github and extract the zip:

.. image:: assets/git-download.png
   :width: 600
   :alt: Download source code from git

Install Necessary Node JS Dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the photon-client directory:

.. code-block:: bash

   npm install

Build and Copy UI to Java Source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the root directory:


.. tab-set::

   .. tab-item:: Linux

      ``./gradlew buildAndCopyUI``

   .. tab-item:: macOS

      ``./gradlew buildAndCopyUI``

   .. tab-item:: Windows (cmd)

      ``gradlew buildAndCopyUI``

Build and Run the Source
~~~~~~~~~~~~~~~~~~~~~~~~

To compile and run the project, issue the following command in the root directory:

.. tab-set::

   .. tab-item:: Linux

      ``./gradlew run``

   .. tab-item:: macOS

      ``./gradlew run``

   .. tab-item:: Windows (cmd)

      ``gradlew run``

Running the following command under the root directory will build the jar under ``photon-server/build/libs``:

.. tab-set::

   .. tab-item:: Linux

      ``./gradlew shadowJar``

   .. tab-item:: macOS

      ``./gradlew shadowJar``

   .. tab-item:: Windows (cmd)

      ``gradlew shadowJar``

Using PhotonLib Builds
~~~~~~~~~~~~~~~~~~~~~~

The build process includes the following task:

.. tab-set::

   .. tab-item:: Linux

      ``./gradlew generateVendorJson``

   .. tab-item:: macOS

      ``./gradlew generateVendorJson``

   .. tab-item:: Windows (cmd)

      ``gradlew generateVendorJson``

This generates a vendordep JSON of your local build at ``photon-lib/build/generated/vendordeps/photonlib.json``.

The photonlib source can be published to your local maven repository after building:

.. tab-set::

   .. tab-item:: Linux

      ``./gradlew publishToMavenLocal``

   .. tab-item:: macOS

      ``./gradlew publishToMavenLocal``

   .. tab-item:: Windows (cmd)

      ``gradlew publishToMavenLocal``

After adding the generated vendordep to your project, add the following to your project's ``build.gradle`` under the ``plugins {}`` block.

.. code-block:: Java

    repositories {
        mavenLocal()
    }

Debugging a local photonvision build
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the program with `./gradlew run --debug-jvm`, and attach to it with VSCode by adding the following to launch.json:

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "type": "java",
            "name": "Attach to Remote Program",
            "request": "attach",
            "hostName": "localhost",
            "port": "5005",
            "projectName": "photon-core",
        }
     ]
]
```

Running examples
~~~~~~~~~~~~~~~~

You can run one of the many built in examples straight from the command line, too! They contain a fully featured robot project, and some include simulation support. The projects can be found inside the photonlib-java-examples and photonlib-cpp-examples subdirectories, respectively. The projects currently available include:

- photonlib-java-examples:
     - aimandrange:simulateJava
     - aimattarget:simulateJava
     - getinrange:simulateJava
     - simaimandrange:simulateJava
     - simposeest:simulateJava
-photonlib-cpp-examples:
     - aimandrange:simulateNative
     - getinrange:simulateNative

To run them, use the commands listed below. Photonlib must first be published to your local maven repository, then the copyPhotonlib task will copy the generated vendordep json file into each example. After that, the simulateJava/simulateNative task can be used like a normal robot project. Robot simulation with attached debugger is technically possible by using simulateExternalJava and modifying the launch script it exports, though unsupported.

```
~/photonvision$ ./gradlew publishToMavenLocal

~/photonvision$ cd photonlib-java-examples
~/photonvision/photonlib-java-examples$ ./gradlew copyPhotonlib
~/photonvision/photonlib-java-examples$ ./gradlew <example-name>:simulateJava

~/photonvision$ cd photonlib-cpp-examples
~/photonvision/photonlib-cpp-examples$ ./gradlew copyPhotonlib
~/photonvision/photonlib-cpp-examples$ ./gradlew <example-name>:simulateNative
```
