    # you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

# Detected time complexity: O(N) total score: 87%

def solution(sizes, directions):
    assert len(sizes) == len(directions)
    is_changed = True
    j = 0  # last eaten fish
    while is_changed:
        is_changed = False
        for i in range(j, len(sizes) - 1):
            p = i
            q = i + 1
            if directions[p] == 1 and directions[q] == 0:
                is_changed = True
                if sizes[p] > sizes[q]:
                    sizes.pop(q)
                    directions.pop(q)
                else:
                    sizes.pop(p)
                    directions.pop(p)
                j = i - 1
                break
    return len(sizes)


assert solution([1, 2], [1, 1]) == 2
assert solution([1, 2], [1, 0]) == 1

assert solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]) == 2
