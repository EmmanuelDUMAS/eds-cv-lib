/* ecv_dilate_3x3_u16.c
 * -----------------------------------------------------------------------------
 * BSD 3-Clause License
 *
 * Copyright (c) 2021, Emmanuel DUMAS
 *
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright
 *   notice, this list of conditions and the following disclaimer.
 * * Redistributions in binary form must reproduce the above copyright
 *   notice, this list of conditions and the following disclaimer in the
 *   documentation and/or other materials provided with the distribution.
 * * Neither the name of the University of California, Berkeley nor the
 *   names of its contributors may be used to endorse or promote products
 *   derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE REGENTS AND CONTRIBUTORS BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
 * ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * -----------------------------------------------------------------------------
 * history
 * 25/01/2021 Creation by copy / paste ecv_dilate_3x3_u16.c ........... E. Dumas
 * -----------------------------------------------------------------------------
 */

#include <common/ecv_errcode.h>
#include <common/ecv_error.h>


tECV_ErrCode ECV_pPixelU16_Dilate3x3(
    const uint8_t *pPixelInU16,
    const int32_t width,
    const int32_t lineStride,
    const int32_t height,
    uint8_t *pPixelOutU16
)
{
  int x,y;

  for(y=1;y<(height-1);y++)
  {
    for(x=1;x<(width-1);x++)
    {
      int max,ix,iy;
      max = pPixelInU16[(x-1) + (y-1) * lineStride];
      for(iy=-1;iy<2;iy++)
        for(ix=-1;ix<2;ix++)
          if (pPixelInU16[(x+ix) + (y+iy) * lineStride] > max)
            max=pPixelInU16[(x+ix) + (y+iy) * lineStride];

      pPixelOutU16[x+y*lineStride] = max;
    }
  }

  return eECV_NoError;
}; /* ECV_pPixelU16_Dilate3x3() */

/* end of file */
