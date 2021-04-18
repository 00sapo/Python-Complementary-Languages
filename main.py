import numpy as np
import time
from typing import List

from julia import Main as list_julia

import list_cy_annotations
import list_cy_annotations_c
import list_py
import list_py_annotations
import list_py_annotations_c
import list_py_c
import simple_list
import list_cy
import list_rust

list_julia.eval('include("list_julia.jl")')

a_list = []  # type: ignore
ttt = time.time()
a_list = list_julia.make_list(a_list)
list_julia.iterate_list(a_list)
print("Julia needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_rust.make_list(a_list)
list_rust.iterate_list(a_list)
print("Rust needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = simple_list.make_list(a_list)
simple_list.iterate_list(a_list)
print("Python needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_py.make_list(a_list)
list_py.iterate_list(a_list)
print("C++ Cython-pure no annotations needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_py_c.make_list(a_list)
list_py_c.iterate_list(a_list)
print("C Cython-pure no annotations needed time: " + str(time.time() - ttt))

_a_list: List[List[float]] = []
ttt = time.time()
_a_list = list_py_annotations.make_list(_a_list)
list_py_annotations.iterate_list(_a_list)
print("C++ Cython-pure pure-annotations needed time: " +
      str(time.time() - ttt))

_a_list = []
ttt = time.time()
_a_list = list_py_annotations_c.make_list(_a_list)
list_py_annotations_c.iterate_list(_a_list)
print("C Cython-pure pure-annotations needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
_a_list = list_cy.make_list(_a_list)
list_cy.iterate_list(_a_list)
print("C Cython needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
_a_list = list_cy_annotations.make_list(_a_list)
list_cy_annotations.iterate_list(_a_list)
print("C++ Cython-pure needed time: " + str(time.time() - ttt))

_a_list = []
ttt = time.time()
_a_list = list_cy_annotations_c.make_list(_a_list)
list_cy_annotations_c.iterate_list(_a_list)
print("C Cython-pure needed time: " + str(time.time() - ttt))
