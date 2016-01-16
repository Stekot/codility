
def solution(l):
    l.sort()
    prev_el = None
    counter = 0
    for el in l:
        if prev_el is None or prev_el != el:
            counter += 1
    return counter

assert solution([2,1,1,2,3,1])
