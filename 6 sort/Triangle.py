def is_triangle(l, p, q, r):
    if not (0 <= p and p < q and q < r):
        return False
    if not (l[p] + l[q] > l[r]):
        return False
    if not (l[q] + l[r] > l[p]):
        return False
    if not (l[r] + l[p] > l[q]):
        return False
    return True


def solution(l):
    n = len(l)
    if n < 3:
        return 0
    l.sort()
    for i in range(n - 2):
        if is_triangle(l, i, i + 1, i + 2):
            return 1
    return 0


assert solution([10, 1, 2, 8, 5, 20]) == 1
assert solution([10, 50, 1, 5]) == 0
