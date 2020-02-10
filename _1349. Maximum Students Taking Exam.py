""" Given a m * n matrix seats  that represent seats distributions in a classroom. If a seat is broken, it is denoted by '#' character otherwise it is denoted by a '.' character.

Students can see the answers of those sitting next to the left, right, upper left and upper right, but he cannot see the answers of the student sitting directly in front or behind him. Return the maximum number of students that can take the exam together without any cheating being possible..

Students must be placed in seats in good condition.

 

Example 1:


Input: seats = [["#",".","#","#",".","#"],
                [".","#","#","#","#","."],
                ["#",".","#","#",".","#"]]
Output: 4
Explanation: Teacher can place 4 students in available seats so they don't cheat on the exam. 
Example 2:

Input: seats = [[".","#"],
                ["#","#"],
                ["#","."],
                ["#","#"],
                [".","#"]]
Output: 3
Explanation: Place all students in available seats. 

Example 3:

Input: seats = [["#",".",".",".","#"],
                [".","#",".","#","."],
                [".",".","#",".","."],
                [".","#",".","#","."],
                ["#",".",".",".","#"]]
Output: 10
Explanation: Place students in available seats in column 1, 3 and 5.
 

Constraints:

seats contains only characters '.' and'#'.
m == seats.length
n == seats[i].length
1 <= m <= 8
1 <= n <= 8 """

import functools
from typing import List
class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m, n = len(seats), len(seats[0])
        @functools.lru_cache(None)
        def dfs_row(pre, r):
            if r == m: return 0
            ne = []
            def dfs(cur, c):
                if c == n:
                    ne.append(cur[:])
                    return
                if seats[r][c] != '#' and (c == n - 1 or not pre[c + 1])  and (c == 0 or not pre[c - 1]) and (c == 0 or not cur[c - 1]):
                    cur[c] = 1
                    dfs(cur, c + 1)
                    cur[c] = 0
                dfs(cur, c + 1)
            dfs([0] * n, 0)
            return  max(sum(cur) + dfs_row(tuple(cur), r + 1) for cur in ne)
        return dfs_row(tuple([0] * n), 0)

s = Solution()
print(s.maxStudents(seats = [["#",".","#","#",".","#"],
                            [".","#","#","#","#","."],
                            ["#",".","#","#",".","#"]])) # 4
print(s.maxStudents(seats = [[".","#"],
                            ["#","#"],
                            ["#","."],
                            ["#","#"],
                            [".","#"]])) # 3
print(s.maxStudents(seats = [["#",".",".",".","#"],
                            [".","#",".","#","."],
                            [".",".","#",".","."],
                            [".","#",".","#","."],
                            ["#",".",".",".","#"]])) # 10