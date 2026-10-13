//! `_bdo_native`, the compiled BDO payload decoders. `paz/native_backend.py`
//! imports it when it is installed; `paz/bdo_decompress.py` and
//! `paz/bdo_ice.py` fall back to Python otherwise.

mod decoder;
mod ice;

use pyo3::exceptions::{PyMemoryError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::PyBytes;

use decoder::UnpackError;
use ice::{CryptError, Subkey};

/// The decompressed bytes of `data[input_start:input_end]`. Raises
/// ValueError with the Python version's error code for a bad stream.
#[pyfunction]
fn unpack<'py>(
    py: Python<'py>,
    data: &[u8],
    input_start: usize,
    input_end: usize,
    decompressed_length: usize,
) -> PyResult<Bound<'py, PyBytes>> {
    // `bytes` cannot change, so the borrow is safe without the GIL, and
    // other threads can decode at the same time.
    let result = py.detach(|| decoder::unpack(data, input_start, input_end, decompressed_length));
    match result {
        Ok(output) => Ok(PyBytes::new(py, &output)),
        Err(UnpackError::Code(code)) => Err(PyValueError::new_err(format!(
            "BDO decompression failed with error code {code}."
        ))),
        Err(UnpackError::OutOfMemory) => Err(out_of_memory(decompressed_length)),
    }
}

/// `data` run through the ICE rounds, one `(k0, k1, k2)` subkey per round.
/// `sbox` is the four S-boxes as 4096 little-endian u32.
#[pyfunction]
fn ice_crypt<'py>(
    py: Python<'py>,
    data: &[u8],
    subkeys: Vec<Subkey>,
    sbox: &[u8],
) -> PyResult<Bound<'py, PyBytes>> {
    let result = py.detach(|| ice::crypt(data, &subkeys, sbox));
    match result {
        Ok(output) => Ok(PyBytes::new(py, &output)),
        Err(CryptError::Invalid(message)) => Err(PyValueError::new_err(message)),
        Err(CryptError::OutOfMemory) => Err(out_of_memory(data.len())),
    }
}

fn out_of_memory(size: usize) -> PyErr {
    PyMemoryError::new_err(format!(
        "cannot allocate {size} bytes for a decoded payload"
    ))
}

#[pymodule]
fn _bdo_native(module: &Bound<'_, PyModule>) -> PyResult<()> {
    module.add_function(wrap_pyfunction!(unpack, module)?)?;
    module.add_function(wrap_pyfunction!(ice_crypt, module)?)
}
