#! /usr/bin/python3
# build.py
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
# Shortcut to all build operation
# -----------------------------------------------------------------------------
# 14/11/2020 Creation ................................................ E. Dumas
# -----------------------------------------------------------------------------

import os
import subprocess

_use_cargo_ = False

if __name__ == "__main__":
    if _use_cargo_:
        subprocess.run(["cargo", "build"], cwd="op_morpho").check_returncode()
    else:
        buildDir = "build"
        if os.path.isdir(buildDir) is False:
            os.makedirs(buildDir)
        
        subprocess.run(["meson", ".."], cwd=buildDir). check_returncode()
        subprocess.run(["ninja"], cwd=buildDir). check_returncode()
    

# read :
# https://git.neosmart.net/mqudsi/meson-rust/src/branch/master/meson.build

# end of file
