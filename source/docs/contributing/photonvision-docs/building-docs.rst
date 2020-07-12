Building the PhotonVision Documentation
=======================================
To build the PhotonVision documentation, you will require `Git <https://git-scm.com>`_ and `Python 3.6 or greater <https://www.python.org>`_.

Cloning the Documentation Repository
------------------------------------
If you are planning on contributing, it is recommended to create a fork of the `main docs repository <https://github.com/PhotonVision/photonvision-docs>`_. To clone this fork, run the following command in a terminal window:

``git clone https://github.com/[your username]/photonvision-docs``

Installing Python Dependencies
------------------------------
You must install a set of Python dependencies in order to build the documentation. To do so, you can run the following command in the root project directory:

``pip install -r requirements.txt``

Building the Documentation
--------------------------
In order to build the documentation, you can run the following command in the root project directory:

``make html``

.. note:: You may have to run ``./make html`` on Windows.

Opening the Documentation
-------------------------
The built documentation is located at ``build/html/index.html``.
