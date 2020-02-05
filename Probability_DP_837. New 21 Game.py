""" Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points, and draws numbers while she has less than K points.  During each draw, she gains an integer number of points randomly from the range [1, W], 
where W is an integer.  Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets K or more points.  What is the probability that she has N or less points?

Example 1:

Input: N = 10, K = 1, W = 10
Output: 1.00000
Explanation:  Alice gets a single card, then stops.
Example 2:

Input: N = 6, K = 1, W = 10
Output: 0.60000
Explanation:  Alice gets a single card, then stops.
In 6 out of W = 10 possibilities, she is at or below N = 6 points.
Example 3:

Input: N = 21, K = 17, W = 10
Output: 0.73278
Note:

0 <= K <= N <= 10000
1 <= W <= 10000
Answers will be accepted as correct if they are within 10^-5 of the correct answer.
The judging time limit has been reduced for this question.
Accepted """

'''
Probability is usually solved by DP, otherwise brute force will take exponential time O(W^K), TLE
First try observe/simulate the process, when you get 0 - K number will not be accepted, after >= K, you will stop, so good number are [K, min(N, K + W)]
if we can sum the probabilities from K to N, then it is our ans
For the each i, the probability of reach i, we can get from the number < i, p[i] = p[i - 1] * 1 / W + p[i - 2] / W + ... + p[p - W] /W
it is liking a fix length sliding window, we can optimize to keep updating wsum to reduce runtime from W to 1 each i
'''

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0: return 1
        p = [1] + [0] * N
        wsum = 1 # for coding elegant, we first calculate this fixed length window sum, and according to condition to update it
        for i in range(1, N + 1):
            p[i] = wsum / W # first calculate the cur p[i]
            if i < K: wsum += p[i] # add into wsum if we can go further for next i
            if i >= W: wsum -= p[i - W] # substract from wsum if we exceed the W length, because each time we at most increase W
                
        return sum(p[i] for i in range(K, N + 1)) 

print(Solution().new21Game(N = 10, K = 1, W = 10)) # 1
print(Solution().new21Game(N = 6, K = 1, W = 10)) # 0.6
print(Solution().new21Game(N = 21, K = 17, W = 10)) # 0.73278
