""" We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef","vyz"].

Suppose we chose a set of deletion indices D such that after deletions, the final array has its elements in lexicographic order (A[0] <= A[1] <= A[2] ... <= A[A.length - 1]).

Return the minimum possible value of D.length.

 

Example 1:

Input: ["ca","bb","ac"]
Output: 1
Explanation: 
After deleting the first column, A = ["a", "b", "c"].
Now A is in lexicographic order (ie. A[0] <= A[1] <= A[2]).
We require at least 1 deletion since initially A was not in lexicographic order, so the answer is 1.
Example 2:

Input: ["xc","yb","za"]
Output: 0
Explanation: 
A is already in lexicographic order, so we don't need to delete anything.
Note that the rows of A are not necessarily in lexicographic order:
ie. it is NOT necessarily true that (A[0][0] <= A[0][1] <= ...)
Example 3:

Input: ["zyx","wvu","tsr"]
Output: 3
Explanation: 
We have to delete every column.
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100 """
# when check every line, if any position is not sorted, delete count + 1. if any position col[i] == col[i + 1], need to keep checking next col
# so we keep a set of rows need to be checked.

class Solution_iteration:
    def minDeletionSize(self, A: List[str]) -> int:
        ans, c_set = 0, set(range(len(A) - 1))
        for col in zip(*A):
            to_rem = set()
            for i in c_set:
                if col[i] > col[i + 1]:
                    ans += 1
                    break
                elif col[i] < col[i + 1]:
                    to_rem.add(i)
            else:
                c_set -= to_rem
        return ans


class Solution_recursion:
    def minDeletionSize(self, A: List[str]) -> int:
        def rec(j, tie):
            if not tie or j == len(A[0]): return 0
            to_rem = set()
            for i in tie:
                if A[i][j] < A[i + 1][j]:
                    to_rem.add(i)
                elif A[i][j] > A[i + 1][j]:
                    return 1 + rec(j + 1, tie)
            return rec(j + 1, tie - to_rem)
        return min(len(A[0]), rec(0, set(range(len(A) - 1))))