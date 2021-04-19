extern crate ndarray;
use ndarray::parallel::prelude::*;
use numpy::{PyArray2, PyReadonlyArray2};
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
fn iterate_list_py<'py>(py: Python<'py>, a_list: PyReadonlyArray2<'_, f64>) -> f64 {
    a_list.as_array().sum()
}

#[pyfunction]
fn iterate_list_multi_py<'py>(py: Python<'py>, a_list: PyReadonlyArray2<'_, f64>) -> f64 {
    a_list.as_array().into_par_iter().sum()
}

#[pyfunction]
fn make_list_py<'py>(py: Python<'py>, a_list: &'py PyArray2<f64>) -> &'py PyArray2<f64> {
    unsafe {
        a_list.as_array_mut().fill(0.01);
    }
    a_list
}

#[pymodule]
fn list_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(iterate_list_py, m)?)
        .unwrap();
    m.add_function(wrap_pyfunction!(iterate_list_multi_py, m)?)
        .unwrap();
    m.add_function(wrap_pyfunction!(make_list_py, m)?).unwrap();

    Ok(())
}
