'''
Given a string, find the length of the longest substring T that contains at most k
distinct characters.
For example, Given s = “eceba” and k = 2,
T is "ece" which its length is 3.
思路：典型的滑动窗口，双指针的问题。如果外面直接套while，太容易写错了。所以直接for loop j。然后移动i来确保每次都是valid的。用res来存最大的结果就行了。
'''

import collections
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        j, res = 0, 0
        m = {}
        for i in range(len(s)):
            m[s[i]] = i
            while len(m) > k:
                if m[s[j]] == j: m.pop(s[j])
                j += 1 
            res = max(res, i - j + 1)
        return res

# test
s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))
