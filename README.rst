Test for lists in cython
========================

Algorithm
---------
1. create a list of 10^4 lists each with 10^4 floats values (namely: 0.1) - 2 nested for
2. iterate each list and compute the cumulative product - 2 netsted for


Implementations
---------------

The real Cython solution is using C++ and ``vector`` type from ``cpplib.vector``.

Another solution is by using Cython in pure-python mode. For some reason here,
an unexpected behavior raise.


Results
-------

+-------------------------------+----------------+---------------------------+---------------------------+
|                               | No annotations | Annotations from `typing` | Annotations from `cython` |
+-------------------------------+----------------+---------------------------+---------------------------+
| Pure Python                   | 11.33          | 11.33                     | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (pure-python mode) | 11.29          | 03.95                     | 05.47                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (pure-python mode)   | 02.77          | 03.21                     | 07.81                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (.pyx)             | -              | -                         | 02.53                     |
+-------------------------------+----------------+---------------------------+---------------------------+

