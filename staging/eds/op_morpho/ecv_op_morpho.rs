// ecv_op_morpho.rs
// ----------------------------------------------------------------------------
// My first try of image processing


#![allow(non_snake_case)]
#![allow(non_camel_case_types)]

// see https://rust-embedded.github.io/book/interoperability/rust-with-c.html
// for explaination on declaration
#[no_mangle]
// https://stackoverflow.com/questions/29182843/pass-a-c-array-to-a-rust-function
pub extern "C" fn ECV_opMorpho(
    pPixelInU8: *const u8,
    width: i32,
    lineStride: i32,
    height: i32,
    pPixelOutU8: *mut u8,
    ) -> i32
{
    let aPxIn = unsafe { std::slice::from_raw_parts(pPixelInU8, (lineStride*height) as usize) };
    let aPxOut = unsafe { std::slice::from_raw_parts(pPixelOutU8, (lineStride*height) as usize) };
    
    println!("The value of width is: {}", width);
    println!("The value of lineStride is: {}", lineStride);
    println!("The value of lineStride is: {}", height);
    println!("The value of 1st pixel is: {}", aPxIn[0]);
    println!("The value of pixel[5] is: {}", aPxIn[5]);
    
    for y in 1..(height-1) {
        // println!("y={}!", y);
        for x in 1..(width-1) {
            
            let mut m:i32=-1;
            
            for ky in -1..1 {
                for kx in -1..1 {
                    let p=aPxIn[ ((x+kx) + (y+ky) * lineStride) as usize];
                    if m > p.into() {
                        m=p.into();
                    }
                    aPxOut[ (x + y * lineStride) as usize] = p;
                }
            }
        }
    }
    
    return 0;
}  // ECV_opMorpho()


// end of file
