import time
from typing import List

from Cython.Build import Cythonize

Cythonize.main(["*[!main.py][!simple_list.py].py", "-3", "--inplace"])
Cythonize.main(["*.pyx", "-3", "--inplace"])

import simple_list
import list_cy
import list_py
import list_py_annotations
import list_cy_annotations
import list_py_c
import list_py_annotations_c
import list_cy_annotations_c

a_list: List[List[float]] = []
ttt = time.time()
simple_list.make_list(a_list)
simple_list.iterate_list(a_list)
print("Python needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
list_py.make_list(a_list)
list_py.iterate_list(a_list)
print("C++ Cython-pure no annotations needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
list_py_c.make_list(a_list)
list_py_c.iterate_list(a_list)
print("C Cython-pure no annotations needed time: " + str(time.time() - ttt))

_a_list: List[List[float]] = []
ttt = time.time()
list_py_annotations.make_list(_a_list)
list_py_annotations.iterate_list(_a_list)
print("C++ Cython-pure pure-annotations needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
list_py_annotations_c.make_list(_a_list)
list_py_annotations_c.iterate_list(_a_list)
print("C Cython-pure pure-annotations needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
list_cy.make_list(a_list)
list_cy.iterate_list(a_list)
print("C++ Cython needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
list_cy_annotations.make_list(a_list)
list_cy_annotations.iterate_list(a_list)
print("C++ Cython-pure needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
list_cy_annotations_c.make_list(a_list)
list_cy_annotations_c.iterate_list(a_list)
print("C Cython-pure needed time: " + str(time.time() - ttt))
