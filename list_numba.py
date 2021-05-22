from numba import njit, prange, typed


@njit
def iterate_list(a_list):
    count: float = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count += a_list[i][j]
    print(count)
    return count


@njit(parallel=False)
def iterate_list_par(a_list):
    count: float = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count += a_list[i][j]
    print(count)
    return count


@njit(parallel=True)
def iterate_list_par_parallel(a_list):
    count: float = 0
    for i in prange(len(a_list)):
        for j in range(len(a_list[i])):
            count += a_list[i][j]
    print(count)
    return count


@njit
def make_list(a_list):
    for i in range(10 ** 4):
        new_list = typed.List()
        for j in range(10 ** 4):
            new_list.append(0.01)
        a_list.append(new_list)
    return a_list


def make_empty_numba_list():
    _nb_a_list = typed.List()

    # add variable, to tell numba the type, then remove it for the benchmark
    dummy = typed.List([0.01])
    _nb_a_list.append(dummy)
    _nb_a_list.pop(0)

    return _nb_a_list
