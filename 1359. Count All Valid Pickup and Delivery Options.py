""" Given n orders, each order consist in pickup and delivery services. 

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i). 

Since the answer may be too large, return it modulo 10^9 + 7.

 

Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90
 

Constraints:

1 <= n <= 500 """
'''
for the i order, previous 2*(i - 1) services
insert first service 2*i - 1, then second 2*i, so total (2*i - 1)*2*i, pickup must be prior to delivery, so need to divide by 2, 2*i^2 - i

The total number of all permutation obviously eauqls to 2n!.
For each pair, the order is determined, so we need to divide by 2.
So the final result is (2n)!/(2^n)
'''
class Solution:
    def countOrders(self, n: int) -> int:
        ans = 1
        for i in range(2, n + 1):
            ans = ans * (2*i*i - i) % 1000000007
        return ans
import math
def countOrders2(self, n):
        return (math.factorial(n * 2) >> n) % (10**9 + 7)

print(Solution().countOrders(1)) # 1
print(Solution().countOrders(2)) # 6
print(Solution().countOrders(3)) # 90