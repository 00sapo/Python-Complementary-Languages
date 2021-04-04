# distutils: language=c++
# cython: language_level=3
from libcpp.vector cimport vector


def iterate_list(vector[vector[float]] a_list):

    cdef float count = 0
    cdef int i, j
    for i in range(a_list.size()):
        for j in range(a_list.size()):
            count *= a_list[i][j]


def make_list(vector[vector[float]] a_list):
    cdef int i, j
    cdef vector[float] new_list
    for i in range(10**4):
        new_list = []
        for j in range(10**4):
            new_list.push_back(0.01)
        a_list.push_back(new_list)
