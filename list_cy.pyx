# cython: language_level=3
# from cython.parallel import prange


cpdef float iterate_list(list a_list):
    cdef double count = 0, d
    cdef int i
    cdef list internal_list
    for internal_list in a_list:
        for d in internal_list:
            count += d
    print(count)
    return count


cpdef list make_list(a_list):
    cdef int i, j
    return [[0.01]*(10**4) for _ in range(10**4)]
