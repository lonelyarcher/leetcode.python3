""" You are given a string s containing lowercase letters and an integer k. You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is palindrome.
Return the minimal number of characters that you need to change to divide the string.

Constraints:

1 <= k <= s.length <= 100.
s only contains lowercase English letters. """
import functools
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        @functools.lru_cache(None)
        def cost(i, j):# mini changes on any subsequence
            if i >= j: return 0
            return (0 if s[i] == s[j] else 1) + cost(i + 1, j - 1)
        @functools.lru_cache(None)
        def dp(i, j, k):
            if k == 1: return cost(i, j) # you need to find out stop limit of i, j and k, k can't be zero, when k == 1, so just call the cost
            if k > j - i + 1: return float('inf') # k also can't exceed the length of targe sequence
            return min((cost(i, p) + dp(p + 1, j, k - 1) for p in range(i, j)), default=0) # the p can't be j, k <= j - l + 1, so l < j - k + 2,  
        return dp(0, len(s) - 1, k)
                

print(Solution().palindromePartition(s = "abc", k = 2)) # 1
print(Solution().palindromePartition(s = "aabbc", k = 3)) # 0
print(Solution().palindromePartition(s = "leetcode", k = 8)) # 0
print(Solution().palindromePartition(s = "leetcode", k = 7)) # 0
print(Solution().palindromePartition(s = "mepekjkpgihfcg", k = 12)) # 0
