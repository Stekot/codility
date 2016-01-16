# https://codility.com/programmers/task/number_of_disc_intersections/
#works but doen't make sence

def solution(l):
    startstop = []
    for i, pos in enumerate(l):
        startstop += [(i - pos, +1), (i + pos, -1)]
    startstop.sort(key=lambda x: (x[0], -x[1]))
    intersection_count = 0
    current_disc_count = 0
    for nyc, difference in startstop:
        if difference > 0:
            intersection_count += current_disc_count
        current_disc_count += difference
        if intersection_count > 10E6:
            return -1
    return intersection_count


assert solution([1, 5, 2, 1, 4, 0]) == 11
# assert solution([1] * 10000000) == -1
