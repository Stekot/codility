# OddOccurrencesInArray
# https://codility.com/programmers/task/odd_occurrences_in_array/
# 100% https://codility.com/demo/results/trainingT7HDAJ-8RQ/

def solution(l):
    n = len(l)
    flag_counter = 0
    assert n % 2 == 1
    for el in l:
        flag_counter = flag_counter ^ el
    return flag_counter


assert solution([1, 2, 1]) == 2
assert solution([1, 2, 1, 2, 4]) == 4
