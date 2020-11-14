// ecv_op_morpho.rs
// ----------------------------------------------------------------------------
// My first try of image processing

// see https://rust-embedded.github.io/book/interoperability/rust-with-c.html
// for explaination on declaration
#[no_mangle]
pub extern "C" fn ECV_opMorpho(width: i32)
{
    println!("The value of width is: {}", width);
}


// end of file
