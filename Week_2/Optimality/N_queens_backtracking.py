
def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in  range(i):
        if i-j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    """
    :param perm: 1 kind of Permutation
    :param n: length of the P / n of the chessboard
    :return:
    """
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            if can_be_extended_to_solution(perm):
                extend(perm, n)

            perm.pop()


extend(perm=[], n=20)
