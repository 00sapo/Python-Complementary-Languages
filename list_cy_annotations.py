# distutils: language=c++

import cython


@cython.locals(i=cython.int, j=cython.int, count=cython.float, a_list=list)
def iterate_list(a_list: list):

    count = 0.0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count = count * a_list[i][j]


@cython.locals(i=cython.int, j=cython.int, new_list=list, a_list=list)
def make_list(a_list: list):
    for i in range(10**4):
        new_list = []
        for j in range(10**4):
            new_list.append(0.01)
        a_list.append(new_list)
