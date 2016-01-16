# MinAvgTwoSlice
# https://codility.com/programmers/task/min_avg_two_slice/
# 60% https://codility.com/demo/results/training64SJ56-7PX/

import sys


def avg(l):
    return float(sum(l)) / len(l)


def solution(l):
    n = len(l)
    min_avg = sys.maxint
    position = -1
    for i in xrange(n - 1):
        start = i
        k = []
        k.append(l[i])
        k.append(l[i + 1])
        while i + 2 < n and l[i + 2] <= 0:
            k.append(l[i + 2])
            i += 1
        local_avg = avg(k)
        if min_avg > local_avg:
            position = start
            min_avg = local_avg
    return position


assert solution([4, 2, 2, 5, 1, 5, 8]) == 1
assert solution([1, 2, -2, 4, -1]) == 1
assert solution([1, 0, -1, -1, 1]) == 2
assert solution([1, 0, 3, 1, -1]) == 3
