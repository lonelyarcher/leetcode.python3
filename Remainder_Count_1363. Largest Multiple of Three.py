""" Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.

 

Example 1:

Input: digits = [8,1,9]
Output: "981"
Example 2:

Input: digits = [8,6,7,1,0]
Output: "8760"
Example 3:

Input: digits = [1]
Output: ""
Example 4:

Input: digits = [0,0,0,0,0,0]
Output: "0"
 

Constraints:

1 <= digits.length <= 10^4
0 <= digits[i] <= 9
The returning answer must not contain unnecessary leading zeros. """

from typing import List
import collections
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = collections.Counter(digits)
        r = sum(digits) % 3
        def output():
            ans = ''
            for i in range(9, -1, -1):
                if cnt[i] > 0: ans += str(i)*cnt[i]
            return '0' if ans == '0'*len(ans) else ans
        def remove(i):
            if i in cnt and cnt[i] > 0:
                cnt[i] -= 1
                if cnt[i] == 0: 
                    del cnt[i]
                return True
            else:
                return False
        if r == 0: 
            return output()
        elif r == 1:
            if remove(1) or remove(4) or remove(7): return output
            elif remove(2, 5) or remove(2, 8) or remove(5, 8): return output
            return ''
        else:
            if remove(2) or remove(5) or remove(8): return output
            elif remove(1, 4) or remove(4, 7) or remove(1, 7): return output
            return ''
print(Solution().largestMultipleOfThree([8,1,9])) # "981"
print(Solution().largestMultipleOfThree([8,6,7,1,0])) # "8760"
print(Solution().largestMultipleOfThree([1])) #
print(Solution().largestMultipleOfThree([0,0,0,0,0,0])) # "0"
