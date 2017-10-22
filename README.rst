pyPhone v0.1
============

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

Supported Python versions
-------------------------

-  Python 3.5

Supported Operating Systems
---------------------------

-  Linux (tested on Ubuntu MATE 17.04 and Raspbian)
-  MacOS (?)
-  Windows (?)

Application icon credits go to:

-  `tango.freedesktop.org <http://tango.freedesktop.org>`__
-  `Google <https://gsuite.google.com/setup/resources/logos/>`__ (for the Google Contacts image)

Release notes
=============

pyPhone v0.1
------------

-  Initial release
