#! /usr/bin/python3
# build_lib_src.py
# -*- coding: utf-8 -*-
# -------------------------------------------------------
# Copyright (c) 2020-2023, Emmanuel DUMAS
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
# Standard lib build
# -----------------------------------------------------------------------------
# 22/11/2020 E. Dumas : creation
# 30/12/2020 E. Dumas : improve error code
# 13/01/2021 E. Dumas : hack for mixing C and Rust
# 28/02/2023 E. Dumas : minor review
# -----------------------------------------------------------------------------

import os
import subprocess

if __name__ == "__main__":
    buildDir = "../lib_build"
    if os.path.isdir(buildDir) is False:
        os.makedirs(buildDir)
    
    # HACK EDS 03/02/2021
    # Today, I haven't found better for compiling mix C/Rust
    home = os.getenv("HOME", ".")
    print("home=", home)
    os.putenv("LD_LIBRARY_PATH", home + "/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib")
    os.environ["LD_LIBRARY_PATH"] = home + "/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib"
    
    subprocess.run(["meson", "../lib_src"], cwd=buildDir). check_returncode()
    subprocess.run(["ninja"], cwd=buildDir). check_returncode()
    

# end of file
