# https://codility.com/programmers/task/perm_missing_elem/
# 100% https://codility.com/demo/results/trainingQKX55Z-FCK/
def solution(l):
    n = len(l)
    if n < 1:
        return 1
    total_sum = 0
    for i in xrange(n + 1):
        if i < n:
            total_sum -= l[i]
        total_sum += i+1
        pass
    return total_sum


assert solution([1, 2, 3, 5, 6]) == 4
assert solution([4, 2, 1, 5, 7, 3]) == 6
assert solution([]) == 1
assert solution([1]) == 2