// ecv_op_morpho.rs
// ----------------------------------------------------------------------------
// My first try of image processing


#![allow(non_snake_case)]
#![allow(non_camel_case_types)]

// see https://rust-embedded.github.io/book/interoperability/rust-with-c.html
// for explaination on declaration
#[no_mangle]
pub extern "C" fn ECV_opMorpho(
    pPixelU8: &u8,
    width: i32,
    lineStride: i32,
    height: i32,
    ) -> i32
{
    println!("The value of width is: {}", width);
    println!("The value of lineStride is: {}", lineStride);
    println!("The value of lineStride is: {}", height);
    println!("The value of 1st pixel is: {}", *pPixelU8);
    
    
    
    return 0;
}  // ECV_opMorpho()


// end of file
