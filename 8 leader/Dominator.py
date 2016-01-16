# https://codility.com/programmers/task/dominator/
import copy


def find_candidate(l):
    assert isinstance(l, list)
    n = len(l)
    if n == 0:
        return None
    j = 0
    changed = True
    # first let's find a candidate
    while changed:
        changed = False
        for i in xrange(j, n - 1):
            if i < j:
                continue
            x = l[i]
            y = l[i + 1]
            if x != y:
                # different elements, remove skip
                j = i + 1
                changed = True
            elif x == y:
                # same values - move to the end
                j = i + 1
                el = l.pop(i)
                l.append(el)
                changed = True
            else:
                print "have we reached the end?"
    return l[-1]


assert find_candidate([1]) == 1
assert find_candidate([1, 2, 2, 3]) == 2
assert find_candidate([1, 2, 1]) == 1
assert find_candidate([2, 2, 1]) == 2
assert find_candidate([1, 2, 2]) == 2
assert find_candidate([1, 1]) == 1
assert find_candidate([2, 1, 3]) is not None
assert find_candidate([]) is None
assert find_candidate([3, 4, 3, 2, 3, -1, 3, 3]) == 3
assert find_candidate([0, 0, 1, 1, 1]) == 1


def solution(l):
    assert isinstance(l, list)
    candidate = find_candidate(copy.copy(l))
    if not l or not candidate or l.count(candidate) / float(len(l)) <= 0.5:
        return -1
    return l.index(candidate)


assert solution([1, 2, 1]) in (0, 2)
assert solution([2, 2, 1]) in (0, 1)
assert solution([1, 2, 2]) in (1, 2)
assert solution([1, 1, 1]) in (0, 1, 2)
assert solution([2, 1, 3]) == -1
assert solution([]) == -1
assert solution([3, 4, 3, 2, 3, -1, 3, 3]) in (0, 2, 4, 6, 7)
assert solution([0, 0, 1, 1, 1]) in (2, 3, 4)
