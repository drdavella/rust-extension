extern crate pyo3;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn print_hello() -> PyResult<()> {
    println!("Hello!");
    println!("Hey again!");

    Ok(())
}

#[pymodule]
fn _corelib(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(print_hello))?;
    Ok(())
}
