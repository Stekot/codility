# https://codility.com/programmers/task/passing_cars/
# PassingCars
# 100%

def solution(A):
    # write your code in Python 2.7
    if len(A) == 0:
        return 0
    e = len([i for i in A if i == 0])
    w = len([i for i in A if i != 0])
    ret = 0
    for a in A:
        if a == 0:
            e-=1
            ret += w
        elif a!=0:
            w-=1
            # print e
            # ret += e
        if ret > 1000000000:
            return -1
    return ret

assert solution([1, 0]) == 0
assert solution([0,0,0,1]) == 3

assert solution([0,1,0,1,1]) == 5

assert solution([]) == 0
assert solution([0,0,0,0]) == 0