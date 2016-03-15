# https://codility.com/programmers/task/perm_check/
# 100% https://codility.com/demo/results/training2MAJ97-EMC/

def solution(l):
    n = len(l)
    positions = [0 for _ in l]
    for number in l:
        number -= 1  # list is indexed from 0
        try:
            positions[number] = 1
        except IndexError:
            return 0
    for check in positions:
        if check == 0:
            return 0
    return 1


assert solution([1, 3, 2, 5, 4]) == 1
assert solution([1, 3, 2, 5, 4, 2]) == 0
assert solution([1, 3, 2, 5]) == 0
