Useful Unix Commands
====================

SSH
---

SSH (Secure Shell) is used to securely connect from a local to a remote system (ex. from a laptop to a coprocessor).

.. note:: Unlike the other commands on this page, ssh is not Unix specific and can be done on Windows and MacOS from their respective terminals.

Example:

.. code-block:: bash

    ssh username@hostname

ifconfig
--------

Run ``ifconfig`` with your coprocessor connected to a monitor in order to see its IP address and other network configuration information.


SCP
---

SCP (Secure Copy) is used to securely transfer files between local and remote systems.

Example:

.. code-block:: bash
    
    scp [file] username@hostname:/path/to/destination

v4l2-ctl
--------

v4l2-ctl is a command-line tool for controlling video devices.

List available video devices (used to verify the device recognized a connected camera):

.. code-block:: bash
    
    v4l2-ctl --list-devices

List supported formats and resolutions for a specific video device:

.. code-block:: bash
    
    v4l2-ctl --list-formats-ext --device /path/to/video_device
