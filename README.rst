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
| Pure Python                   | 11.08          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (pure-python mode) | 02.25          | 02.81                     | 02.96                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (pure-python mode)   | 02.23          | 02.97                     | 02.91                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (.pyx)               | -              | -                         | 02.77                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| Julia (pyjulia)               | 03.50          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| Julia (pyjulia) parallel      | 02.11          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| Rust (Pyo3) parallel before   | 08.72          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| Rust (Pyo3) parallel after    | 29.17          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+

Cython is fast, but none of these methods are able to release the GIL. Moreover,
in pure-python mode, Cython effectiveness decreases while using typing
annotations. Last but not least, it's hard to understand which solution is
better with Cython. The average time is 2.7

Rust is not that fast beacuse it needs to copy data; using Pyo3 objects would
probably lead to similar results as cython, but with an added library.
Moreover, it's tricky because after having run some code its perfomance
decreases.

Numba is still tricky with lists. I tried to use them, but it fails. In my
experience, numba lists in nopython mode slows down the code.

Julia is fast (only 30% slower than the average Cython). With multithreading
it's even faster than Cython.

Considering echosystem, multithreading and ease of use, Julia is a clear winner here.
