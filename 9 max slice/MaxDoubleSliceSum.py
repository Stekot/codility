# https://codility.com/programmers/task/max_double_slice_sum/
# 53% https://codility.com/demo/results/trainingEK9HDT-ANM/

def find_x(l):
    # let's find left border of slice
    sum_max = None
    i_max = None
    for i, el in enumerate(l):
        sum_sofar = sum(l[i + 1:])
        if sum_sofar is None or sum_sofar > sum_max:
            sum_max = sum_sofar
            i_max = i
    return i_max


assert find_x([1, -3, 3, 1, 4, 2, -1]) == 1
assert find_x([-2, -3, -4, 1, -5, -6, -7]) == 3

def find_z(l, x):
    n = len(l)
    i_max = None
    sum_max = None
    for i in xrange(n - 1):
        i = n - i - 1
        if i <= x:
            continue
        if x + 2 >= i:
            continue
        sum_sofar = sum(l[:i])
        if sum_sofar is None or sum_sofar > sum_max:
            sum_max = sum_sofar
            i_max = i
    return i_max


assert find_z([1, -3, 3, 1, 4, 2, -1], x=1) == 6
assert find_z([3, 2, 6, -1, 4, 5, -1, 2], x=0) == 6
assert find_z([0, 10, -5, -2, 0], x=0) == 3


def find_y(l, x, z):
    assert x + 1 < z
    n = len(l)
    sum_total = sum(l)
    sum_max = None
    y = None
    for i, el in enumerate(l):
        if not (x < i < z):
            continue
        sum_sofar = sum_total - el
        if sum_max is None or sum_max < sum_sofar:
            y = i
            sum_max = sum_sofar
    return y


assert find_y([1, -3, 3, 1, 4, 2, -1], x=1, z=6) == 3


def max_none(*args):
    return max([a for a in args if a is not None])


def solution(l):
    n = len(l)
    if n == 3:
        return 0
    x = find_x(l)
    assert x
    z = find_z(l, x=x)
    assert z
    y = find_y(l, x=x, z=z)
    assert x < y < z
    if x > 0 and l[x] < l[y]:
        return sum(l[x + 1:z])
    if z < n - 1 and l[z] > l[z + 1]:
        return sum(l[x + 1:z])
    return sum(l[x + 1:z]) - l[y]


# assert solution([1, 2, 2, 1, 2, 1]) == 6
# assert solution([1, 1, 1]) == 0
# assert solution([1, -3, 3, 1, 4, 2]) == 8
# assert solution([3, 2, 6, -1, 4, 5, -1, 2]) == 17
# assert solution([0, 10, -5, -2, 0]) == 10
# assert solution([-8, 10, 20, -5, -7, -4]) == 30
assert solution([-2, -3, -4, 1, -5, -6, -7])
