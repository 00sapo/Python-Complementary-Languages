from typing import List

from numba import njit, prange, typed, float64


@njit
def iterate_list(a_list):

    count: float = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count += a_list[i][j]
    print(count)
    return count


@njit(parallel=True)
def iterate_list_par(a_list):

    count: float = 0
    for i in prange(len(a_list)):
        for j in range(len(a_list[i])):
            count += a_list[i][j]
    print(count)
    return count


@njit
def make_list(a_list):
    for i in range(10**4):
        new_list = typed.List(float64)
        for j in range(10**4):
            new_list.append(0.01)
        a_list.append(new_list)
    return a_list
