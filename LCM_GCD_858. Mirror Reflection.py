""" There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.



Note:

1 <= p <= 1000
0 <= q <= p """
import math
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        #lcm = p * q / math.gcd(p, q)
        def gcd(p, q):
            p, q = max(p, q), min(p, q)
            return q if p % q == 0 else gcd(p % q, q)
        lcm = p * q / gcd(p, q)
        m, n = lcm / q, lcm / p
        if m % 2 and n % 2: return 1
        if not m % 2 and n % 2: return 2
        else: return 0
print(Solution().mirrorReflection(p = 2, q = 1)) #2
print(Solution().mirrorReflection(p = 3, q = 1)) #1
print(Solution().mirrorReflection(p = 1, q = 2)) #0