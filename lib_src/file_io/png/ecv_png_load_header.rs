// ecv_png_load_headers.rs
// ----------------------------------------------------------------------------
// Copyright (c) 2021, Emmanuel DUMAS
// All rights reserved.
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
//
// * Redistributions of source code must retain the above copyright
//   notice, this list of conditions and the following disclaimer.
// * Redistributions in binary form must reproduce the above copyright
//   notice, this list of conditions and the following disclaimer in the
//   documentation and/or other materials provided with the distribution.
// * Neither the name of the University of California, Berkeley nor the
//   names of its contributors may be used to endorse or promote products
//   derived from this software without specific prior written permission.
//
// THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
// EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
// DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
// THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
// ----------------------------------------------------------------------------
// ECV Png tools : load header
// ----------------------------------------------------------------------------
// History
// 02/01/2021 Creation ............................................... E. Dumas
// ----------------------------------------------------------------------------

#![allow(non_snake_case)]
#![allow(non_camel_case_types)]


fn ECV_templatePureRust(
    pPixelInU8: &[u8],
    width: i32,
    lineStride: i32,
    height: i32,
    pPixelOutU8: &mut [u8],
    ) -> i32
{
    
    
    println!("PR The value of width is: {}", width);
    println!("PR The value of lineStride is: {}", lineStride);
    println!("PR The value of lineStride is: {}", height);
    println!("PR The value of 1st pixel is: {}", pPixelInU8[0]);
    println!("PR The value of pixel[5] is: {}", pPixelInU8[5]);
    
    for y in 1..(height-1) {
        // println!("y={}!", y);
        for x in 1..(width-1) {
            
            let mut m:u8=0;
            
            for ky in -1..1 {
                for kx in -1..1 {
                    let p=pPixelInU8[ ((x+kx) + (y+ky) * lineStride) as usize];
                    if m < p {
                        m=p;
                    }
                    
                }
            }
            pPixelOutU8[ (x + y * lineStride) as usize] = m;
            
        }
    }
    
    return 0;
}  // ECV_templatePureRust()



// see https://rust-embedded.github.io/book/interoperability/rust-with-c.html
// for explaination on declaration
#[no_mangle]
pub extern "C" fn ECV_PNG_LoadHeader(
    ) -> i32
{
    println!("ECV_PNG_LoadHeader() - 00");
    
    println!("ECV_PNG_LoadHeader() - 99");
    return 0;
}  // ECV_PNG_LoadHeader()

// end of file
