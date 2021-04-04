# distutils: language=c++

from typing import List
import cython


def iterate_list(a_list: List[List[float]]):

    count = cython.declare(cython.float, 0.0)
    i = cython.declare(cython.int, 0)
    j = cython.declare(cython.int, 0)
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count *= a_list[i][j]


def make_list(a_list: List[List[float]]):
    i = cython.declare(cython.int, 0)
    j = cython.declare(cython.int, 0)
    for i in range(10**4):
        new_list = []
        for j in range(10**4):
            new_list.append(0.01)
        a_list.append(new_list)
