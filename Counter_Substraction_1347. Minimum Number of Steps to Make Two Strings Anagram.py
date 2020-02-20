""" Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
Example 4:

Input: s = "xxyyzz", t = "xxyyzz"
Output: 0
Example 5:

Input: s = "friend", t = "family"
Output: 4
 

Constraints:

1 <= s.length <= 50000
s.length == t.length
s and t contain lower-case English letters only. """

# counter substraction, will ignore negative counter, so only count A - B, where char in A's occurrance is greater than B.
# since A and B are same length, whenever A has one more char count that B, which also means in other char, there is one more count in B, 
# replace it in one place will fix both side mismatch, mini replacement will be the sum of values of A - B 

import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = collections.Counter(s) - collections.Counter(t)
        return sum(diff.values())