# https://codility.com/programmers/task/min_perimeter_rectangle/
# 100% https://codility.com/demo/results/training6EMBYU-WDH/

def get_divs(n):
    i = 1
    divs = set()
    while (i * i < n):
        if (n % i == 0):
            divs.add(i)
            divs.add(n / i)
        i += 1
    if (i * i == n):
        divs.add(i)
    return sorted(list(divs))


def solution(N):
    divs = get_divs(N)
    A = divs[len(divs) / 2]
    B = N / A
    return 2 * (A + B)

assert solution(30) == 22
