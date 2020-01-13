""" Return the number of distinct non-empty substrings of text that can be written as the concatenation of some string with itself.

 

Example 1:

Input: text = "abcabcabc"
Output: 3
Explanation: The 3 substrings are "abcabc", "bcabca" and "cabcab".
Example 2:

Input: text = "leetcodeleetcode"
Output: 2
Explanation: The 2 substrings are "ee" and "leetcodeleetcode".
 

Constraints:

1 <= text.length <= 2000
text has only lowercase English letters. """

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n, mod, ans = len(text), 1000000007, set()
        pow = [1]
        for _ in range(n): pow.append(pow[-1] * 31)
        c = lambda i: ord(text[i]) - ord('a') + 1
        def hash(i, j):
            h = 0
            for k in range(j - i):
                h += c(i + k) * pow[k]
            return h
        for l in range(2, n + 1, 2):
            h1, h2 = hash(0, l//2), hash(l//2, l)
            if h1 == h2: ans.add(text[:l])
            for i in range(1, n - l + 1):
                h1 = ((h1 + mod - c(i - 1) * pow[l//2 - 1]) * 31 + c(i + l//2 - 1)) % mod
                h2 = ((h2 + mod - c(i + l//2 - 1) * pow[l//2 - 1]) * 31 + c(i + l - 1)) % mod
                if h1 == h2: ans.add(text[i:i + l])
        print(ans)
        return len(ans)
                
s1 = Solution()
print(s1.distinctEchoSubstrings("leetcodeleetcode")) #2
print(s1.distinctEchoSubstrings("abcabcabc")) #3



# s2 = Solution()
# print(s2.distinctEchoSubstrings()) #
# print(s2.distinctEchoSubstrings()) #
