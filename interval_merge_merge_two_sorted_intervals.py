'''
Given two sorted interval list by start, merge them into one sorted interval list
example:
A = [[0, 1], [2, 4], [5, 6], [8, 11], [12, 15]]
B = [[3, 10]]
output: [[0, 1], [2, 11], [[12, 15]]]

'''

import collections

class Solution:
    def merge(self, A, B):
        i, j, ans = 0, 0, []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                ans.append(A[i])
                i += 1
            elif A[i][0] <= B[j][1] and B[j][0] <= A[i][1]:
                B[j] = [min(B[j][0], A[i][0]), max(B[j][1], A[i][1])]
                i += 1
            else:
                ans.append(B[j])
                j += 1
        ans.append(A[i:] if i < len(A) else B[j:])
        return ans
A = [[0, 1], [2, 4], [5, 6], [8, 11], [12, 15]]
B = [[3, 10]]
print(Solution().merge(A, B))
