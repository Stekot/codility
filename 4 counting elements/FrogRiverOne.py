# https://codility.com/programmers/task/frog_river_one/
# 100% https://codility.com/demo/results/trainingPEV7Y6-8BY/

def solution(end, l):
    position = 0
    n = len(l)
    end = max(l)
    river = [0 for _ in range(end)]
    for t, leaf in enumerate(l): # t - time
        leaf -= 1
        river[leaf] = 1
        while position < end and river[position] == 1:
            position += 1
        if position >= end:
            return t
    return -1


assert solution(6, [1,2,3,4,5,6]) == 5
assert solution(4, [1, 3, 1, 4, 2, 3, 5, 4]) == 6

assert solution(5, [1,2,3,1,2,5]) == -1
assert solution(6, [1,2,6]) == -1
