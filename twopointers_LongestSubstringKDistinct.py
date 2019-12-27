'''
Given a string, find the length of the longest substring T that contains at most k
distinct characters.
For example, Given s = “eceba” and k = 2,
T is "ece" which its length is 3.




i, j fast/slow pointers, use a dict to record last occupancy position of character
when more than K distinct characters, move the slow pointer j to the most left ( smallest ) last occupancy position
then update the res of i - j, delete/pop this last occupancy key from dict
'''


class Solution(object):

    def lengthOfLongestSubstringKDistinct(self, s, k):
        res, j = 0, -1 # init j = -1, then i - j = len(s) when k > distinct char in s 
        m = {}
        for i,c in enumerate(s):
            m[c] = i
            if len(m) > k:
                j = min(m.values())
                m.pop(s[j])
            res = max(res, i - j)
        return res

# test
s = "eceba"
k = 2
print(Solution().lengthOfLongestSubstringKDistinct(s, k))
