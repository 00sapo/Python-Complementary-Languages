Test for lists in cython
========================

Algorithm
---------
1. create a list of 10^4 lists each with 10^4 floats values (namely: 0.1) - 2 nested for
2. iterate each list and compute the cumulative product - 2 netsted for


Implementations
---------------

* Julia using Julia objects
* Rust using Rust objects
* Pure-python
* Cython pure-python mode with no annotations
* Cython pure-python mode with Python annotations
* Cython pure-python mode with Cython annotations
* Standard Cython

Setup
-----

* `poetry install --no-root`
* `poetry run python setup.py build_ext --inplace`
* `poetry run python -c "import julia; julia.install()"`

Results
-------

* `poetry run python main.py`


Tested on:

* Intel Core i5-8250U - 64 bits - Quad Core L2 cache: 6 MiB
* Linux 5.4.105-1-MANJARO x86_64
* GCC 10.2.0
* Python 3.9.2
* Cython 0.29.17
* Julia 1.6
* Cargo 1.51

+-------------------------------+----------------+---------------------------+---------------------------+
|                               | No annotations | Annotations from `typing` | Annotations from `cython` |
+-------------------------------+----------------+---------------------------+---------------------------+
| Pure Python                   | 11.13          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (pure-python mode) | 02.16          | 03.25                     | 03.04                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (pure-python mode)   | 02.78          | 03.07                     | 02.83                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (.pyx)               | -              | -                         | 02.98                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| Julia (pyjulia)               | 03.63          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| Rust (Pyo3)                   | 17.02          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+

Cython is fast, but none of these methods are able to release the GIL. Moreove,
in pure-python mode, cython effectiveness decreases while using typing
annotations.

Considering echosystem, multithreading and ease of use, Julia is a clear winner here.

