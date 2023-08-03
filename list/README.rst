Python Complementary Languages
==============================

This repository contains a small benchmark to see which language is better to speedup computations when Python lists of lists are used

Algorithm
---------
1. Create a list of 10^4 lists each with a number of floats defined by the the argument; the float
   value is arbitrary (e.g. 0.1)
2. Iterate each list and compute the cumulative product - 2 nested for

Algorithms using arrays instead of lists/vectors are not valid.

The aim of the algorithm is to prove ability in data sharing from Python to the
complementary language and back, including counting precision with little numbers.

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
* Install python 3.11.4: ``PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.11.4``
* Install pdm: ``curl -sSL https://pdm.fming.dev/install-pdm.py | python3 - ``
* Install Cargo, Nim, C/C++ compiler
* Install project dependencies: ``pdm install -v`` (create virtualenv, install
  pakages, and compile). **When prompted for recompiling PyCall, choose option 2.
  (recompile) and optionally restart the installtion if it fails**

N.B. ``PYTHON_CONFIGURE_OPTS="--enable-shared"`` is needed for pyjulia to work.

Results
-------

* ``
* ``pdm run python main.py``
``


Tested on:

* CPU: 14-core 12th Gen Intel Core i9-12900H (-MST AMCP-)
speed/min/max: 2413/400/4900:5000:3800 MHz
* Linux 6.1.41
* GCC 13.1.1
* Python 3.11.4
  Cython 3.0.0
* Julia 1.9.2
* Cargo 1.71.0
* Nim 1.6.10


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
