""" Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef". """

'''
use recursion to parse, keep i pointer as nonlocal variable, you can use self.i too.
the recursion function will return parsed output (string or map or result number)
in function, first define the result variable for following loop
while loop after, you can first think if there is no recursion parenthesis, just concate the each reading character to the ans
then usually if char is  ())[ ] or number, means recursion begins, you can call the parse function recursively here and add it to the ans
at last, when you finish the while loop, which means either you reach the end of string if you are in first layer of parsing function, 
or you reach the end )] which means you finish the current layer of recursion.


outside the recursion method, just call the parse and return it.
'''
class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        def parse():
            nonlocal i
            ans = ''
            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    n = 0
                    while s[i].isdigit():
                        n = n * 10 + int(s[i])
                        i += 1 # don't forget move the point in the while loop
                    i += 1 # handle [
                    ans += "".join(parse() * n)
                else:
                    c = s[i]
                    ans += c
                i += 1
            return ans
        return parse()