#!/usr/bin/python3
# tst_png_load_header.py
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2021, Emmanuel DUMAS
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
# Template file for EDS-CV-Lib Project - test file
# -----------------------------------------------------------------------------
# History
# 19/10/2020 Creation ................................................ E. Dumas
# -----------------------------------------------------------------------------

# native python import
import os
import subprocess
import unittest

# third party import
import cffi
# import numpy as np

# project import

# tested file
# from lib_src.file_io.png import ecv_png_load_header


# -----------------------------------------------------------------------------
# Class
# -----------------------------------------------------------------------------
class TST_PNG_LoadHeader(unittest.TestCase):
    """Test load header functions
    02/01/2021 Creation .............................................. E. Dumas
    """
    
    def setUp(self):
        """
        02/01/2021 Creation .......................................... E. Dumas
        """
        print("setup")
        
        soPath = "../../../lib_build/file_io/libecv_file_io.so"
        
        if os.path.isfile(soPath) is False:
            Exception("file '%s' not found" % soPath)
        
        self.ffi = None
        self.ffi = cffi.FFI()
        
        self.lib = None
        self.lib = self.ffi.dlopen(soPath, flags=self.ffi.RTLD_GLOBAL)
    
    def tearDown(self):
        """
        02/01/2021 Creation .......................................... E. Dumas
        """
        print("tearDown")
    
    def commonPart(self):
        """
        19/10/2020 Creation .......................................... E. Dumas
        """
        print("common part")
    
    def test_Dataset_01(self):
        """call test with data set 01 : ...
        19/10/2020 Creation .......................................... E. Dumas
        """
        print("test Dataset 01")
        
        self.commonPart()
        
        # c = eds_template.EDS_Template()
        # self.assertNotEqual(c, None)
    
    def test_Dataset_02(self):
        """call test with data set 02 : ...
        19/10/2020 Creation .......................................... E. Dumas
        """
        print("test Dataset 02")
        
        self.commonPart()
        
        self.ffi.cdef("""int32_t ECV_PNG_LoadHeader(
            );
        """)
        
        ret = self.lib.ECV_PNG_LoadHeader()
        self.assertNotEqual(ret, 0)
    

# -----------------------------------------------------------------------------
# Test suite definition
# -----------------------------------------------------------------------------
def TST_TestSuite_PNG_LoadHeader(testSuite, oneByOne=False):
    """
    19/10/2020
    """
    allTests = (
        "test_Dataset_01",
        # "test_Dataset_02",
    )
    
    if oneByOne is True:
        runTests = (allTests[0], )
    else:
        runTests = allTests
    
    for t in runTests:
        testSuite.addTest( TST_PNG_LoadHeader( t ) )
    

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    r = subprocess.run( ["python3", "build_lib_src.py", ],
                        cwd="../../..")
    print("r=", r.returncode)
    if r.returncode == 0:
        testSuite = unittest.TestSuite()
        TST_TestSuite_PNG_LoadHeader(testSuite, oneByOne=False)
        unittest.TextTestRunner(verbosity=2).run(testSuite)


# end of file
