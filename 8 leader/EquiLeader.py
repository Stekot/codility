# Detected time complexity: O(N ** 2)

from collections import Counter


class EquailLeader(object):
    l = None
    l1 = None
    l2 = None

    def __init__(self, l):
        self.l = l  # original list to be iterated
        self.l1 = Counter([])  # first list
        self.l2 = Counter(l)  # second list
        self.counter = 0
        self.n = float(len(self.l))

    def count_leaders(self):
        for i, el in enumerate(self.l):
            self.l1[el] += 1
            self.l2[el] -= 1
            cand1 = self.get_leader(self.l1, i + 1)
            cand2 = self.get_leader(self.l2, self.n - i - 1)
            if cand1 == cand2 and cand1 is not None:
                self.counter += 1
        return self.counter

    def get_leader(self, l, n):
        assert sum(l.values()) == n
        if n < 1:
            return None
        candidate, freq = l.most_common()[0]
        if freq <= n / 2.0:
            return None
        return candidate


def solution(l):
    equal_leader = EquailLeader(l)
    return equal_leader.count_leaders()


assert solution([1, 2]) == 0
assert solution([]) == 0
assert solution([4, 3, 4, 4, 4, 2]) == 2
