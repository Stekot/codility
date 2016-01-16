# https://codility.com/programmers/task/frog_jmp/
# 100% https://codility.com/demo/results/trainingQS9ZAU-Z6N/
import math

def solution(x, y, d):
    return int(math.ceil( # round float up
        float(y - x) / d
    ))


assert solution(1, 5, 2) == 2
assert solution(1, 100, 30) == 4
assert solution(10, 85, 30) == 3
