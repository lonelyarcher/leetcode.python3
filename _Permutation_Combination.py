import itertools
def permutations(A, n):
    A.sort() # for later avoiding repeat
    ans, seen = [], [False] * len(A)
    def permute(path):
        if len(path) == n:
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

def combinations_with_replacement(A, n):
    ans = []
    def rec(path, i):
        if len(path) == n:
            ans.append(tuple(path))
        else:
            for j in range(i, len(A)):
                path.append(A[j])
                rec(path, j) # difference, can repeat itself
                path.pop()
    rec([], 0)
    return ans

print(permutations([1, 1, 2, 1], 2))
print(list(itertools.permutations([1, 1, 2, 1], 2))) # include repeat

print(combinations([1, 2, 3, 4, 5], 3))
print(list(itertools.combinations([1, 2, 3, 4, 5], 3)))

print(combinations_with_replacement([1, 2, 3], 3))
print(list(itertools.combinations_with_replacement([1, 2, 3], 3)))