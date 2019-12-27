""" Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000 """

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        l, r, ans = 0, len(A) - 1, -float("inf")
        # two pointers template, while: if r-- else l++, every while loop just do one side shrink for on step. To avoid check the condition again in the loop.
        while l < r:
            if A[l] + A[r] >= K:  # only one place to check the condition
                r -= 1
            else:
                ans = max(ans, A[l] + A[r])
                l += 1
        return -1 if ans == -float("inf") else ans