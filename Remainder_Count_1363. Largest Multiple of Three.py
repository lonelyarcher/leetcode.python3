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


'''
O(n) time complexity, remainder = sum(digits) % 3 will have three cases: 
1. r == 0: concat the digits following the descendant order will be the answer
2. r == 1: 
    if digits have 1, 4, 7, then remove one is the answer, of course order is 1, 4, 7. 
    if not, then need remove two of 2, 5, 8. We can use a trick, try to remove two 2, two 5, then two 8, if we can get r % 3 == 0, then stop
3. r == 2: 
    same as r==1, first remove 2, 5, 8, then two of 1, 4, 7, until r % 3 == 0
output, need consider '', '00000' -> 0, and use count sort to achieve O(n) time.
'''

from typing import List
import collections
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        cnt = collections.Counter(digits)
        r = sum(digits) % 3
        def remove(i):
            if cnt[i] > 0:
                cnt[i] -= 1
                if cnt[i] == 0: 
                    del cnt[i]
            if sum(i * cnt[i] for i in cnt) % 3 == 0: 
                return True
            else: 
                return False
        if r == 1 and cnt[1] + cnt[4] + cnt[7]:
            remove(1) or remove(4) or remove(7)
        elif r == 2 and cnt[2] + cnt[5] + cnt[8]:
            remove(2) or remove(5) or remove(8)
        elif r == 1:
            remove(2) or remove(2) or remove(5) or remove(5) or remove(8) or remove(8) # use 'or' to achieve to r%3==0, once achieve then stop
        elif r == 2:
            remove(1) or remove(1) or remove(4) or remove(4) or remove(7) or remove(7)
        if len(cnt) == 1 and 0 in cnt: return '0'
        return "".join(str(i)*cnt[i] for i in range(10)[::-1])
print(Solution().largestMultipleOfThree([8,1,9])) # "981"
print(Solution().largestMultipleOfThree([8,6,7,1,0])) # "8760"
print(Solution().largestMultipleOfThree([1])) #
print(Solution().largestMultipleOfThree([0,0,0,0,0,0])) # "0"
