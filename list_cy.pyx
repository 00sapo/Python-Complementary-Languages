# cython: language_level=3
from cython.parallel cimport prange
from cython.view cimport array as cvarray
cimport openmp, cython

cdef float sum_list(double[:] a_list) nogil:
    cdef double internal_count = 0
    for j in range(a_list.shape[0]):
        with cython.boundscheck(False):
            internal_count += a_list[j]
    return internal_count

cpdef float iterate_list(double[:,:] a_list):
    cdef double count = 0
    cdef int i, j
    for i in prange(a_list.shape[0], nogil=True):
        count += sum_list(a_list[i, :])
    print(count)
    return count


cpdef double[:,:] make_list(a_list):
    cdef int i, j
    cdef double[:,:] my_list = cvarray(shape=(10**4, 10**4), itemsize=sizeof(double), format="d")
    for i in prange(my_list.shape[0], nogil=True):
        for j in range(my_list.shape[1]):
            with cython.boundscheck(False):
                my_list[i, j] = 0.01
    return my_list
