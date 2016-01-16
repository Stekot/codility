# https://codility.com/programmers/task/missing_integer/
# 100% https://codility.com/demo/results/trainingFYKEAZ-G4X/


def solution(l):
    l = set([val for val in l if val > 0])
    l = sorted(l)
    for i, val in enumerate(l):
        if val != i + 1:
            return i + 1
    return len(l) + 1


assert solution([1, 2, 3, 4, 5]) == 6
assert solution([-1, 4, 3, 2, 1, -4, 5, 7]) == 6
assert solution([1, 3, 6, 4, 1, 2]) == 5
