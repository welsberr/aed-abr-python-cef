"""
Avida-ED ABR (anti-bit-rot)

This is an attempt to package together everything needed to run Avida-ED-Eco:
server and browser and code, so that we can pass executables along without
fear that some library change somewhere will make it obsolete.


"""
import sys
import os
import traceback
import time
import platform
from cefpython3 import cefpython as cef
#from http.server import HTTPServer, SimpleHTTPRequestHandler

import threading
import http.server
import socket 
from http.server import HTTPServer, SimpleHTTPRequestHandler

import requests



# Server info
# https://stackoverflow.com/questions/24580613/python-start-http-server-in-code-create-py-to-start-http-server

def launch_server(servedir="Avida-ED-Eco", serveport=8847):
    absservedir = os.path.abspath(servedir)
    print(servedir, absservedir)
    os.chdir(absservedir)
    httpd = None
    server = None

    """
    try:
        httpd = HTTPServer(('localhost', serveport), SimpleHTTPRequestHandler)
        httpd.serve_forever()
    except:
        httpd.shutdown()
        httpd = None
    """
    
    try:
        debug = True
        server = http.server.ThreadingHTTPServer((socket.gethostname(), serveport), SimpleHTTPRequestHandler)
        if debug:
            print("Starting Server in background")
            thread = threading.Thread(target = server.serve_forever)
            thread.daemon = True
            thread.start()
        else:
            print("Starting Server")
            print('Starting server at http://{}:{}'.format(socket.gethostname(), serveport))
            server.serve_forever()

    except:
        server.shutdown()
        server = None
        
    return server

def close_server(httpd):
    if not httpd in [None]:
        httpd.shutdown()

def main():
    check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    cef.Initialize()
    cef.CreateBrowserSync(url="https://www.google.com/",
                          window_title="Hello World!")
    cef.MessageLoop()
    cef.Shutdown()


def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"


def launch_aed_browser(url="http://localhost:8847/index.html", title="Avida-ED-Eco ABR (CEF 66)"):
    print("launch_aed_browser() start...")
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {
        "debug": True,
        "log_severity": cef.LOGSEVERITY_INFO,
        "log_file": "debug.log",
        #"auto-open-devtools-for-tabs": True,
    }
    cef.Initialize(settings=settings)
    cef.CreateBrowserSync(url=url,
                          window_title=title)
    cef.MessageLoop()
    cef.Shutdown()
    

if __name__ == '__main__':

    # Launch server
    print("Launching server.")
    httpd = launch_server()
    print("After server launch.")

    assert not httpd in [None], "Fatal error: Failed to launch Avida-ED-Eco ABR (CEF 66.0) local server process."

    # Give the server a little time to come up
    time.sleep(4)

    print("Server launched, now launching browser.")

    # Launch browser
    launch_aed_browser()

    # Shutdown server
    close_server(httpd)

    print("Avida-ED-Eco ABR (CEF 66.0) done.")
    
    
    
