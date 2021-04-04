def iterate_list(a_list):

    count = 0
    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            count *= a_list[i][j]


def make_list(a_list):
    for i in range(10**4):
        new_list = []
        for j in range(10**4):
            new_list.append(0.01)
        a_list.append(new_list)
