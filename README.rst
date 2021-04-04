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

Tested on 
- Intel Core i5-8250U - 64 bits - Quad Core L2 cache: 6 MiB
- Linux 5.4.105-1-MANJARO x86_64
- GCC 10.2.0
- Python 3.9.2
- Cython 0.29.17

+-------------------------------+----------------+---------------------------+---------------------------+
|                               | No annotations | Annotations from `typing` | Annotations from `cython` |
+-------------------------------+----------------+---------------------------+---------------------------+
| Pure Python                   | 11.22          | -                         | -                         |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (pure-python mode) | 02.69          | 03.80                     | 05.37                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C Cython (pure-python mode)   | 02.66          | 03.13                     | 08.27                     |
+-------------------------------+----------------+---------------------------+---------------------------+
| C++ Cython (.pyx)             | -              | -                         | 02.39                     |
+-------------------------------+----------------+---------------------------+---------------------------+

