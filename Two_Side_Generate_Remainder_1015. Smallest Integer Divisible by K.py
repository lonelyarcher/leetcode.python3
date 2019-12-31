""" Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only contains the digit 1.

Return the length of N.  If there is no such N, return -1.

 

Example 1:

Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.
Example 2:

Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.
Example 3:

Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.
 

Note:

1 <= K <= 10^5 """

'''
First K * ? = 111..1, From one end, if we can find this ? , then we can calculate the 11...1 and count it, return the ans
but ? can be very large, brute force to generate from 1 to big integer, will TLE
So from another side, let's generate 111...1, which it takes log(N), better
But this question, 111...1 can be unlimited, so still problem.
only K is relative small number < 10^5
Trick is when we add 1 to the right of 111..1 as p = p * 10 + 1, we can take % K , so p % K == p * 10 % K if p is not 2 or 5 's mul
we knew K can not be even number and 5's multiplication. so the equation is valid. 
then we know if we met the same remainder again, it means no answer, return -1
we can use a set to record all the previous remainder
or use pigeon cage principal, if we do K time still can't fine 0, then must one remainder are repeated, then we can stop the while loop and return -1
'''

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0: return -1
        p = 1
        for i in range(K):
            if p % K == 0: return i + 1
            p = (p * 10 + 1) % K
        return -1