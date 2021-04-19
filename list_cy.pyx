# cython: language_level=3
# from cython.parallel import prange


cpdef float iterate_list(a_list):

    cdef double count = 0
    cdef int i, j
    for i in range(len(a_list)):
        internal_list = a_list[i]
        for j in range(len(internal_list)):
            count += internal_list[j]
    print(count)
    return count


cpdef list make_list(a_list):
    cdef int i, j
    for i in range(10**4):
        new_list = []
        for j in range(10**4):
            new_list.append(0.01)
        a_list.append(new_list)
    return a_list
