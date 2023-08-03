use pyo3::prelude::*;
use pyo3::wrap_pyfunction;
use rayon::prelude::*;

#[pyfunction]
fn iterate_list(py: Python, a_list: Vec<Vec<f64>>) -> f64 {
    // let count = a_list.iter().map(|l| l.iter().sum::<f64>()).sum::<f64>();
    let count = py.allow_threads(|| a_list.par_iter().map(|l| l.iter().sum::<f64>()).sum::<f64>());
    println!("{}", count);
        
    return count;
}

#[pyfunction]
fn make_list(mut a_list: Vec<Vec<f64>>) -> Vec<Vec<f64>> {
    for _i in 0..i64::pow(10, 4) {
        let mut new_list = Vec::<f64>::new();
        for _j in 0..i64::pow(10, 4) {
            new_list.push(0.01_f64);
        }
        a_list.push(new_list);
    }
    return a_list;
}

#[pymodule]
fn list_rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(iterate_list, m)?).unwrap();
    m.add_function(wrap_pyfunction!(make_list, m)?).unwrap();

    Ok(())
}
