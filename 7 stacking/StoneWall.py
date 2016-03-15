def solution(l):
    # block_counts = get_blocks(h)
    # return block_counts
    blocks = 0  # number of blocks
    stack = []
    for h in l:
        pass
        if len(stack) == 0 or h > stack[-1]:
            stack.append(h)
            blocks += 1
        else:
            while len(stack) and h < stack[-1]:
                stack.pop()
            if len(stack) == 0 or h > stack[-1]:
                stack.append(h)
                blocks += 1
        pass
    return blocks


assert solution([4, 6, 4, 3]) == 3
assert solution([4, 6, 4, 3, 4]) == 4
assert solution(reversed([4, 6, 4, 3, 4])) == 4
assert solution([8, 8, 5, 7, 9, 8, 7, 4, 8]) == 7
assert solution([6, 6, 4, 4, 4, 7, 8, 7, 3, 3]) == 5
