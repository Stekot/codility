# GenomicRangeQuery
# https://codility.com/programmers/task/genomic_range_query/
# 100% https://codility.com/demo/results/trainingQ2RYNA-J2S/

def solution(S, P, Q):
    n = len(S)
    map_values = {"A": 1, "C": 2, "G": 3, "T": 4}
    occours = {"A": [0] * (n + 1), "C": [0] * (n + 1), "G": [0] * (n + 1), "T": [0] * (n + 1)}
    for i, letter in enumerate(S):
        for l in "ACGT":
            occours[l][i + 1] = occours[l][i]
        occours[letter][i + 1] += 1
    for l in "ACGT":
        assert len(occours[l]) == n + 1
    assert len(P) == len(Q)
    m = len(P)
    ret_values = [0] * m
    for j in range(m):
        if P[j] == Q[j]:
            ret_values[j] = map_values[S[P[j]]]
            continue
        for l in "ACGT":
            if occours[l][P[j]] != occours[l][Q[j] + 1]:
                ret_values[j] = map_values[l]
                break
    assert len(ret_values) == m
    return ret_values


assert solution("CAGCCTA", [5], [5]) == [4]
assert solution("CAGCCTA", [2, 5, 0], [4, 5, 6]) == [2, 4, 1]
assert solution('AC', [0], [1]) == [1]
assert solution('AC', [0, 0, 1], [0, 1, 1]) == [1, 1, 2]
assert solution('TC', [0, 0, 1], [0, 1, 1]) == [4, 2, 2]
