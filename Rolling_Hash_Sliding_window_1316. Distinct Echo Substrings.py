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
    def distinctEchoSubstrings0(self, text: str) -> int:
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
    '''
    Better solution for rolling hash, try inserting a line between two index, like a|b|c|a|b|c, expanding from each line, 
    if left part == right part, then it is a echo substring
    while expanding, left part always add one char to its head, and right part alway add one char to its tail, we can use rolling hash to reduce compare string to O(1)
    so total time will be O(n^2) 
    '''
    def distinctEchoSubstrings(self, text: str) -> int:
        n, mod, ans = len(text), 1000000007, set()
        pow = [1] #rolling hash, always calculate the pow array
        for i in range(n): pow.append(pow[-1] * 31)
        c = lambda i: ord(text[i]) - ord('a') + 1
        for i in range(n - 1):
            h1, h2 = c(i), c(i + 1)
            if h1 == h2: ans.add(text[i: i + 2])
            for j in range(1, min(i + 1, n - (i + 1))):
                h1 = (h1 + c(i - j) * pow[j]) % mod
                h2 = (h2 * 31 + c(i + j + 1)) % mod
                if h1 == h2: ans.add(text[i - j:i + j + 2])
        print(ans)
        return len(ans)
    ''' best O(n^2) solution without rolling hash. 
    for every substring, n^2, first iterate by len, then for this length, we move the beginning point i from left to right
    text = eabcabc
    for length 3, e a b | c a b => e a b   => count 2 matches, a == a and b == b, if we move a step to right a b c | a b c, a == a, b == b matches are kept
                                   c a b 
    we add new incoming match c == c, remove the previous pair e != c, we do the same rolling matches, when total match count == 3, we add it into the set                               
    '''
    def distinctEchoSubstrings2(self, text: str) -> int:
        ans, n = set(), len(text)
        for l in range(2, n + 1, 2):
            match = sum(a == b for a, b in zip(text[:l//2], text[l//2:l]))
            if match == l//2: ans.add(text[:l])
            for i in range(n - l + 1):
                match += (text[i + l - 1] == text[i + l//2 - 1]) - (text[i - 1] == text[i + l//2 - 1])
                if match == l//2: ans.add(text[i:i + l])
        return len(ans)
        
                
s1 = Solution()
print(s1.distinctEchoSubstrings("leetcodeleetcode")) #2
print(s1.distinctEchoSubstrings("abcabcabc")) #3
print(s1.distinctEchoSubstrings2("leetcodeleetcode")) #2
print(s1.distinctEchoSubstrings2("abcabcabc")) #3





# s2 = Solution()
# print(s2.distinctEchoSubstrings()) #
# print(s2.distinctEchoSubstrings()) #
