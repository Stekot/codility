# CountDiv
# https://codility.com/programmers/task/count_div/
# 100% https://codility.com/demo/results/trainingPT4RQS-MP3/

def solution(A, B, K):
    # write your code in Python 2.7
    if A % K == 0:
        return (B - A) / K + 1
    else:
        return (B - A + (A % K)) / K

assert solution(6,11,2) == 3
assert solution(5,5,5) == 1
assert solution(10,20,3) == 3