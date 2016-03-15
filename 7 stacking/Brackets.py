
def solution(S):
    # write your code in Python 2.7
    if len(S) % 2 == 1:
        return 0
    stack = []
    try:
        for ch in S:
            assert ch in "(){}[]"
            if ch == "(":
                stack.append("(")
            elif ch == ")" and stack[-1] == "(":
                stack.pop()
            elif ch == "[":
                stack.append("[")
            elif ch == "]" and stack[-1] == "[":
                stack.pop()
            elif ch == "{":
                stack.append("{")
            elif ch == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return 0
    except IndexError:
        return 0
    return 1 * (len(stack) == 0)

assert solution("([{)") == 0
assert solution("((()") == 0
assert solution("())(()()") == 0
assert solution("(())") == 1
assert solution("(()(())())") == 1
assert solution(")(") == 0
assert solution("") == 1