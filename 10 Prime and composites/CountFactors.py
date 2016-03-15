# https://codility.com/programmers/task/count_factors/
# 100% https://codility.com/demo/results/trainingD23K2X-6BR/
from math import sqrt


def solution(n):
    i = 1
    divs = set()
    while (i * i < n):
        if (n % i == 0):
            divs.add(i)
            divs.add(n/i)
        i += 1
    if (i * i == n):
        divs.add(i)
    return len(divs)

assert solution(24) == 8
