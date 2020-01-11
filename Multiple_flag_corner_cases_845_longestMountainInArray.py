""" Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000
Follow up:

Can you solve it using only one pass?
Can you solve it in O(1) space? """
from typing import List
# one pointer but multiple flags or state variables
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        cur, ans, peaked, started = 0, 0, False, False
        for i in range(1, len(A)):
            if A[i] == A[i - 1] or not started and A[i - 1] > A[i] or peaked and A[i - 1] < A[i]:
                if peaked: 
                    ans = max(ans, cur + 1)
                cur, peaked, started = 0, False, False
                if A[i - 1] < A[i]: 
                    cur, started = 1, True
            else:
                cur, started = cur + 1, True
                if i > 1 and A[i - 2] < A[i - 1] > A[i]:
                    peaked = True
        ans = max(ans, cur + 1) if peaked else ans
        return ans if ans >= 3 else 0
# two pointers, l (base, stop at left boundary of mountain array), r (fast/end pointer to go through a mountain and stop at right boundary), better solution
    def longestMountain_twopointers(self, A: List[int]) -> int:
        N = len(A)
        ans = base = 0
        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: #if base is left-boundary of mountain
                while end+1 < N and A[end] < A[end + 1]:
                    end += 1 # moving the end to the peak
                if end + 1 < N and A[end] > A[end + 1]: #if end is really a peak..
                    while end + 1 < N and A[end] > A[end+1]: 
                        end += 1 # move the end to right-boundary of mountain
                    ans = max(ans, end - base + 1) #record candidate answer
            base = max(end, base + 1) # move the base, either end or +1
        return ans