#! /usr/bin/python3
# edsimgviewer.py
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# Copyright (c) 2020, Emmanuel DUMAS
# All rights reserved.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the University of California, Berkeley nor the
#   names of its contributors may be used to endorse or promote products
#   derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------
# Image viewer for EDS-CV-Lib
#
#    this image have an launcher in python, but most of viewer must be
#    develop in javascript / html
#
# -----------------------------------------------------------------------------
# 15/10/2020 Creation ................................................ E. Dumas
# 20/10/2020 Set file as args ........................................ E. Dumas
# 29/12/2020 First operational version ............................... E. Dumas
# -----------------------------------------------------------------------------

import argparse
import http.server
# import inspect
import os
import socketserver
import subprocess
from functools import partial
from multiprocessing import Process


def basicHttpServer():
    """Start a basic HTTP server
    15/10/2020 creation EDS
    """
    # start a web server
    PORT = 8008
    # Handler = http.server.SimpleHTTPRequestHandler
    HandlerClass = partial( http.server.SimpleHTTPRequestHandler,
                            directory="/")
    
    with socketserver.TCPServer(("", PORT), HandlerClass) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs='*')
    parser.add_argument("-d", action="store_true")
    args = parser.parse_args()
    print("args=", args)
    # print("args.files=", args.files)
    #    ->args.files= ['f1', 'f2', 'f3']
    
    pserv = Process(target=basicHttpServer)
    pserv.start()
    
    curPath = os.path.normpath( os.path.join( os.getcwd(),
                                              os.path.dirname(__file__ ) ) )
    # print("curPath=", curPath)
    # curPath= /home/xxx/working/eds-cv-lib/tools/edsimgviewer
    
    secArg = "http://127.0.0.1:8008" + curPath + "/load_img.html"
    if len(args.files) == 1:
        secArg += "?f1=%s" % (os.getcwd() + "/" + args.files[0])
    elif len(args.files) >= 2:
        secArg += "?f1=%s&f2=%s" % (os.getcwd() + "/" + args.files[0],
                                    os.getcwd() + "/" + args.files[1])
    
    lArgs = [ "firefox", secArg ]
    if args.d:
        lArgs.append("-jsconsole")
    
    pLauncher = subprocess.run( lArgs )
    
    pserv.join()
    

# end of file
