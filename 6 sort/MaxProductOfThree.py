# https://goo.gl/js2NVV
# 100%

class HeapSort(object):
    l = []
    n = None
    size = None

    def __init__(self, l):
        self.l = l
        self.size = len(self.l)

    def get(self, pos):
        return self.l[pos - 1]

    def switch(self, pos1, pos2):
        self.l[pos1 - 1], self.l[pos2 - 1] = self.l[pos2 - 1], self.l[pos1 - 1]

    def heapify(self, end=None):
        if end is None:
            end = self.size
        for i in range(end):
            pos = self.size - i
            pos2 = pos / 2
            if pos == 1:
                continue
            if self.get(pos) > self.get(pos2):
                self.switch(pos, pos2)
        print self.l[:end], self.l[end:]


    def sift(self):
        pass

    def sort(self):
        self.heapify()
        end = self.size
        while end > 0:
            self.switch(0, end)
            end -= 1
            self.heapify(end)


# l = [1, 2, 3, 4]
# l1 = l
# h = HeapSort(l1)
# h.switch(1, 2)
# assert h.l == [2, 1, 3, 4]
#
# l1 = l
# h = HeapSort(l1)
# h.heapify()
# for pos, el in enumerate(h.l):
#     try:
#         assert el == max(h.l[pos], h.l[pos * 2])
#         assert el == max(h.l[pos], h.l[(pos * 2) + 1])
#     except IndexError:
#         pass



def solution(l):
    h = HeapSort(l)
    h.sort()
    return max(h.l[-1] * h.l[-2] * h.l[-3],
               h.l[-1] * h.l[0] * h.l[1])

solution([3, 7, 4, 7, 9])
# assert solution([3, 4, 2]) == 24
# assert solution([3, 7, 4, 7, 9]) == 441
# assert solution([-3, 1, 2, -2, 5, 6]) == 60
# assert solution([5, -6, 3, -7, -3, 4]) == 210
