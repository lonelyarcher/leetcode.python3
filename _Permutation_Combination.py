import itertools
def permutations(A):
    A.sort() # for later avoiding repeat
    ans, seen = [], [False] * len(A)
    def permute(path):
        if len(path) == len(A):
            ans.append(tuple(path))
        else:
            for j in range(len(A)):
                if seen[j] or j > 0 and A[j] == A[j - 1] and not seen[j - 1]: continue # avoid repeat, if repeat sequence, can only pick first one at first time.
                seen[j] = True
                path.append(A[j])
                permute(path)
                seen[j] = False
                path.pop()
    permute([])
    return ans

def combinations(A, n):
    ans = []
    def rec(path, i):
        if len(path) == n:
            ans.append(tuple(path))
        else:
            for j in range(i, len(A)):
                path.append(A[j])
                rec(path, j + 1)
                path.pop()
    rec([], 0)
    return ans

print(permutations([1, 1, 1]))
print(list(itertools.permutations([1, 1, 1]))) # include repeat

print(combinations([1, 2, 3, 4, 5], 3))
print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))