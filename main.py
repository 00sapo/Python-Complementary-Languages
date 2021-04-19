import os
import time
from typing import List
# from numba import typed, types, float64

from julia.api import LibJulia  # noqa: autoimport
api = LibJulia.load()  # noqa: autoimport
api.init_julia(["--project=.", "--optimize=3", f"--threads={os.cpu_count()}"])  # noqa: autoimport
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
# import list_numba

list_julia.eval('include("list_julia.jl")')
list_julia.eval('include("list_julia_threads.jl")')

_a_list: List[List[float]]

# _nb_a_list = typed.List(typed.List(float64))
# ttt = time.time()
# _nb_a_list = list_numba.make_list(_nb_a_list)
# list_numba.iterate_list_par(_nb_a_list)
# print("Numba needed time: " + str(time.time() - ttt))

# _nb_a_list = NBList()  # type: ignore
# ttt = time.time()
# _nb_a_list = list_numba.make_list(_nb_a_list)
# list_numba.iterate_list(_nb_a_list)
# print("Numba multi-threading needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_rust.make_list(a_list)
list_rust.iterate_list(a_list)
print("Rust multithreading before needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_julia.make_list(a_list)
list_julia.iterate_list(a_list)
print("Julia needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_julia.make_list(a_list)
list_julia.Threaded.iterate_list(a_list)
print("Julia multi-threading needed time: " + str(time.time() - ttt))

a_list = []  # type: ignore
ttt = time.time()
a_list = list_rust.make_list(a_list)
list_rust.iterate_list(a_list)
print("Rust multithreading after needed time: " + str(time.time() - ttt))

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

_a_list = []
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
