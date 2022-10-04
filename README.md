# aed-abr-python-cef

## Avida-ED-Eco Anti-Bit Rot Python: CEFPython approach

## Initial pass ##

This is the start of experimenting with use of CEFPython to
package the Avida-ED-Eco web app for deployment to multiple
host platforms while keeping a fixed browser so that
the version as it stands can have long-term stability
for use into the future.

## Prerequisites ##

To develop and build the project, Python 3.7 and required packages
need to be installed.

## Organization ##

This top-level directory contains one necessary file:

* aedabrcef.py

The contents of the Avida-ED-Eco Git repository must be
added to the Avida-ED-Eco directory.

## Operations ##

Run the program as:

> python aedabrcef.py

The Python 3 'http' module's 'server' is invoked in its own thread and
serves files out of the Avida-ED-Eco directory, accessed with:

> http://localhost:8847/index.html

This has been verified by loading that URL in a regular
browser tab.

The program pauses for 5 seconds, then launches an instance
of the embedded CEF browser which is passed the same url.

## Deployment

It is expected that an approach like this should allow packaging to
a single-file executable using a tool like 'cx_freeze' or 'pyinstaller'.
This has not yet been checked.

## Issues ##

1. Avida-ED-Eco/index.html does not load in the CEF browser instance.

2. CEF browser does not respond to F12 or ctrl-shift-J to launch DevTools.

