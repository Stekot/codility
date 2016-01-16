# https://codility.com/programmers/task/binary_gap/
# 100% https://codility.com/demo/results/trainingNEYAF6-DKP/
# BinaryGap

def solution(N):
    bin = '{0:b}'.format(N)
    bin = bin.strip('0')
    counter = 0
    ret_value = 0
    for el in bin:
        assert el in ("0","1")
        if el == "1":
            counter = 0
        else:
            counter += 1
            ret_value = max(ret_value, counter)
    return ret_value

assert solution(1) == 0
assert solution(1041) == 5
assert solution(6) == 0