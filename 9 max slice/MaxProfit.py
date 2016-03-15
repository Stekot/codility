#https://codility.com/programmers/task/max_profit/
# 100% https://codility.com/demo/results/training8ETJH4-VV5/

def solution(l):
    max_profit = 0
    high_idx = None
    high = None
    low_idx = None
    low = None
    for i, el in enumerate(l):
        if high is None or el > high:
            high = el
            high_idx = i
        assert high == l[high_idx]
        if low is None or el < low:
            low = el
            low_idx = i
            high = el
            high_idx = i
        assert low <= high
        assert low == l[low_idx]
        assert low_idx <= high_idx
        if max_profit < high - low:
            max_profit = high - low
    return max(max_profit, 0)


assert solution([1,2]) == 1
assert solution([23171, 21011, 21123, 21366, 21013, 21367]) == 356