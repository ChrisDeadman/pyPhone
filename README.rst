pyPhone 1.0.0a2
===============

Author: ChrisDeadman

Minimalistic phone client using `python-gammu <https://github.com/gammu/python-gammu>`__.

This is what pyPhone was created for (so don't expect it to look great on a desktop screen, lol):

|pyPhone_in_action|

.. |pyPhone_in_action| image:: https://raw.githubusercontent.com/ChrisDeadman/pyPhone/master//pyPhone_in_action.jpeg

Feature list
------------

-  Make outgoing calls
-  Receive incoming calls
-  Monitor phone and connection status
-  Load google contacts via Google People API v1

TODO list
---------

-  SMS support
-  Phone-stored contacts support
-  Call mangling support (?)
-  Calender support (?)

Known Issues
------------

-  **Answering a call does not show ongoing call window for 30-60secs**
      | *This was a bug in libgammu and has been* `fixed here <https://github.com/gammu/gammu/commit/ac5106175fdea7622772be46f1221cd66a24ec58#diff-0ce4149983bed46e06d03ae69aab2206>`__.
      | *You might need to install a newer libgammu from source depending on your distro.*

Installing
----------

You can install the usual way for python modules using distutils, so use
``setup.py`` which is placed in the top level directory::

    python3 setup.py build
    sudo python3 setup.py install

Logging
-------

Since this is an early version it may be neccesary to check ``~/.pyPhone/pyPhone.log`` in case something is not working.

Change ``level`` in ``~/.pyPhone/pyPhone.config`` to either one of ``DEBUG, INFO, WARNING, ERROR, CRITICAL``
to increase or decrease the log level::

    [LOGGING]
    level = DEBUG

Google People API
-----------------

To support loading contacts from your google account, enter
``client-id`` and ``client-secret`` in ``~/.pyPhone/pyPhone.config``:

::

    [GAUTH]
    client-id = your_client_id
    client-secret = your_client_secret

Those can be obtained by `creating a google API
key <https://console.developers.google.com/apis/>`__ (enable *Google People API*)

Required versions
-----------------

-  Python >= 3.5
-  libgammu >= 1.38.6

Supported Operating Systems
---------------------------

-  Linux (tested on Ubuntu and Raspbian)
-  MacOS (?)
-  Windows (?)

Application icon credits go to:

-  `tango.freedesktop.org <http://tango.freedesktop.org>`__
-  `Google <https://gsuite.google.com/setup/resources/logos/>`__ (for the Google Contacts image)

Release notes
=============

pyPhone 1.0.0a2
---------------

-  Bugfix: fix calls not detected after error-status during answering
-  Bugfix: fix event detection delay by using ReadDevice() for polling
-  Display more phone information on the information screen

pyPhone 1.0.0a1
---------------

-  Initial release
