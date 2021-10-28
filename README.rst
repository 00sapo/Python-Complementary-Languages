Python Complementary Languages
==============================

This repository contains a small benchmark to see which language is better to speedup computations when Python lists of lists are used

Algorithm
---------
1. Create a list of 10^4 lists each with 10^4 floats values (namely: 0.01) - 2 nested for
2. Iterate each list and compute the cumulative product - 2 nested for

Algorithms that use numpy arrays instead of lists are not valid.

Implementations
---------------

* Julia using Julia objects
* Rust using Rust objects
* Pure-python
* Numba
* Cython pure-python mode with no annotations
* Cython pure-python mode with Python annotations
* Cython pure-python mode with Cython annotations
* Standard Cython
* Nim lang

Setup
-----
* Install pyenv: ``curl https://pyenv.run | bash; exec $SHELL``
* Install python 3.9.6: ``PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.9.6``
* Install poetry: ``curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -``
* Install project dependencies: ``poetry install --no-root``
* ``poetry run python setup.py build_ext --inplace``
* ``poetry run nim c -d:danger --out:list_nim.so list_nim.nim``

N.B. ``PYTHON_CONFIGURE_OPTS="--enable-shared"`` is needed for pyjulia to work.

Results
-------

* ``poetry run python main.py``


Tested on:

* Intel Core i5-8250U - 64 bits - Quad Core L2 cache: 6 MiB
* Linux 5.4.105-1-MANJARO x86_64
* GCC 10.2.0
* Python 3.9.2
* Cython 0.29.17
* Julia 1.6
* Cargo 1.51
* Nim 1.4.6


**Pure python time (reference): 11.03 s**

Compiled-based languages
~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+----------------+---------------------------+---------------------------+
|                               | No annotations | Annotations from `typing` | Annotations from `cython` |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (pure-python mode) | 02.42          | 02.98                     | 02.92                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (pure-python mode)   | 02.40          | 02.97                     | 02.87                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (.pyx)               | -              | -                         | 00.81                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| Rust (PyO3) parallel 1st run  | 07.40          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| Rust (PyO3) parallel 2nd run  | 09.45          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| Nim                           | 05.59          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+

JIT-based languages
~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------+----------------+-----------+
|                               | Second run     | First Run |
+-------------------------------+----------------+-----------+
| Julia (pyjulia)               | 00.83          | 02.46     |
+-------------------------------+----------------+-----------+
| Julia (pyjulia) parallel      | 00.52          | 01.12     |
+-------------------------------+----------------+-----------+
| Numba                         | 04.88          | 05.58     |
+-------------------------------+----------------+-----------+
| Numba parallel                | 02.75          | 03.30     |
+-------------------------------+----------------+-----------+

Cython is fast, but none of these methods are able to release the GIL. Moreover,
in pure-python mode, Cython effectiveness decreases while using typing
annotations. Last but not least, it's hard to understand which solution is
better with Cython. The average time is 2.48 s.

Rust is not that fast beacuse it needs to copy data; using Pyo3 objects would
probably lead to similar results as cython, but with an added library.
Moreover, it's tricky because after having run some code its perfomance
decreases.

Similarly to Rust, Nim suffers from copying data too.

Numba is still tricky with lists. Performance is encouraging, but the code is
not intuitive at all and requires a lot of hacks, breaking the pythonic
language.

Julia is fast as much as Cython and with multithreading it's even faster!
Considering echosystem, multithreading and ease of use, Julia is a clear winner
here.

Note, however, that `pyjulia` cannot be run in multiple python subprocesses,
which is a shame for parallelizeing code at the process level -- e.g. for speeding-up tests, etc.
It's then much easier to use Python from Julia using PyCall module.
