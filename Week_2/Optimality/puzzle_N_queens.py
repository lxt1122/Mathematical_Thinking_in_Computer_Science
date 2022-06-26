# Question 5
#
# Place 8 queens such that no two attack each other.

#  Is it possible to place n queens on an n*n chessboard such that no 2 queens attack each other?
#  1.single Q in each row/column/diagonal


import itertools as it


def is_solution(perm):
    for (i1, i2) in it.combinations(range(len(perm)), 2):
        if abs(i1 - i2) == abs(perm[i1] - perm[i2]):
            return False

    return True


for perm in it.permutations(range(8)):
    if is_solution(perm):
        print(perm)
        exit()
