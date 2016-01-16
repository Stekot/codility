
def solution(S):
    # write your code in Python 2.7
    if len(S) % 2 == 1:
        return 0
    stack_count = 0
    for ch in S:
        if stack_count < 0:
            return 0
        if ch == "(":
            stack_count += 1
        elif ch == ")":
            stack_count -= 1
    return 1 * stack_count == 0

assert solution("((()") == 0
assert solution("())(()()") == 0
assert solution("(()(())())") == 1
assert solution("") == 1