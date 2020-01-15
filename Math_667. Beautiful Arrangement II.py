""" Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement:
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:
Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:
Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:
The n and k are in the range 1 <= k < n <= 104. """

'''

O(n), to has K distinct differences, we know [1, 2, 3, .., n] only has 1 diff, 
so we can make first k + 1 elements to make k distinct diff, then all after are in order which diff = 1
like [1, 4, 2, 3, 5, 6, 7] for n = 7 and k = 3 distinct diff, 1, 1 + k, 1 + k - (k - 1), ...

or first k elements has k - 1 diff without 1, then the left in order
[1, 7, 2, 3, 4, 5, 6] for n = 7 , k = 3, two pointers pick from left and right to implement

for ans, always easy to create a empty and append/insert for original list. Don't try to do it in place, in-place is harder
to shift +/- or dir in loop, use a sign *= -1 or judge by odd/even len or i are both OK.
be careful to the range end excluding 
'''

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans, sign = [1], 1
        for i in range(k, 0, -1):
            ans.append(ans[-1] + sign * i)
            sign *= -1
        ans.extend(range(k + 2, n + 1))
        return ans
    
    def constructArray_2(self, n: int, k: int) -> List[int]:
        l, r, ans = 1, n, []
        for i in range(k):
            if i % 2 == 0:
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        if len(ans) % 2 == 1:
            ans.extend(range(l, r + 1))
        else:
            ans.extend(range(r, l - 1, -1))
        return ans
