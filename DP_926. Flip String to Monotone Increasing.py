""" A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.
 

Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters. """

# DP is easy and fast O(n), but need lucky you begin with it not greedy, greedy is not working but it take time to findout
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        ans, zero = 0, 0 # zero is min flips to all zero
        for s in S:
            if s == '1':
                ans = min(ans, zero) # prior to update zero
                zero += 1
            else:
                ans = 1 + min(ans, zero) 
        return min(zero, ans)