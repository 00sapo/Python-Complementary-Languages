# distutils: language = c
from typing import List


def iterate_list(a_list: List[List[float]]):

    count: float = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count *= a_list[i][j]


def make_list(a_list: List[List[float]]):
    for i in range(10**4):
        new_list = []
        for j in range(10**4):
            new_list.append(0.01)
        a_list.append(new_list)
