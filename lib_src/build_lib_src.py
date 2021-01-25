#! /usr/bin/python3
# build_lib_src.py
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# BSD 3-Clause License
#
# Copyright (c) 2020-2021, Emmanuel DUMAS
# All rights reserved.
#
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
# Standard lib build
# -----------------------------------------------------------------------------
# 22/11/2020 Creation ................................................ E. Dumas
# 30/12/2020 Improve error code ...................................... E. Dumas
# 13/01/2021 Hack for mixing C and Rust .............................. E. Dumas
# 25/01/2021 Can use CMake now ....................................... E. Dumas
# -----------------------------------------------------------------------------

import os
import subprocess


def buildWithMeson():
    """Build with Meson Build
    22/11/2020 Creation E. Dumas
    """
    # HACK EDS 03/02/2021
    # Today, I haven't found better for compiling mix C/Rust
    home = os.getenv("HOME", ".")
    print("home=", home)
    os.putenv("LD_LIBRARY_PATH", home + "/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib")
    os.environ["LD_LIBRARY_PATH"] = home + "/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib"
    
    subprocess.run(["meson", "../lib_src"], cwd=buildDir). check_returncode()
    subprocess.run(["ninja"], cwd=buildDir). check_returncode()
    

def buildWidthCMake():
    """Build with CMake
    18/01/2021 Creation E. Dumas
    """
    subprocess.run(["cmake", "../lib_src"], cwd=buildDir). check_returncode()
    subprocess.run(["cmake", "--build", "."], cwd=buildDir). check_returncode()
    

if __name__ == "__main__":
    buildDir = "../lib_build"
    if os.path.isdir(buildDir) is False:
        os.makedirs(buildDir)
    
    # buildWithMeson()
    buildWidthCMake()
    
# end of file
