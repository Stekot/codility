# https://codility.com/programmers/task/tape_equilibrium/
# TapeEquilibrium
# 100% https://codility.com/demo/results/trainingMXT5X8-RJ6/
import sys


def solution(l):
    n = len(l)
    total_sum = sum(l)
    minimum_sum = sys.maxint
    sum1 = 0
    sum2 = total_sum
    for i in xrange(n - 1):
        sum1 += l[i]
        sum2 -= l[i]
        current_sum = abs(sum1 - sum2)
        minimum_sum = min(current_sum, minimum_sum)
        pass
    return minimum_sum


assert solution([-1000, 1000]) == 2000
assert solution([3, 1, 2, 4, 3]) == 1
