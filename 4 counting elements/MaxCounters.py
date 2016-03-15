# https://codility.com/programmers/task/max_counters/

class Counter:
    l = []
    n = None
    max_value = None
    used_max_value = None

    def __init__(self, n):
        self.l = [0 for _ in xrange(n)]
        self.n = n

    def eval(self, x):
        if 1 <= x <= self.n:
            self.increase(x)
        elif x == self.n + 1:
            self.max_counter()
        else:
            print "error"

    def increase(self, pos):
        pos -= 1
        self.l[pos] = self.value(pos) + 1
        self.max_value = max(self.max_value, self.l[pos])

    def max_counter(self):
        self.used_max_value = self.max_value

    def value(self, pos):
        return max(self.used_max_value, self.l[pos])

    def results(self):
        return [self.value(i) for i in xrange(self.n)]


def solution(n, l):
    c = Counter(n)
    for el in l:
        c.eval(el)
        # print c.results()
    return c.results()


assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == [3, 2, 2, 4, 2]
