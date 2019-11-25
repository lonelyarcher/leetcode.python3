""" You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1 """


import collections
from typing import List
class Solution:
    def countServers_UF(self, grid: List[List[int]]) -> int:
        """ UF on all cells, 
        1. UF on N nodes from 0 to N-1 or 1 to N which has connection
        2. UF on all nodes include those empty cells which will not has connection. It is fine it just connect to itself which need exclude in collecting steps
        3. UF on a map of object/string/int, not continuous number.
        All three are fine for UF, you can choose upon the question, here we choose the second one which looks easy to implements
        """
        m, n = len(grid), len(grid[0])
        p = [i for i in range(m * n)]
        def find(i):
            if p[i] != i: p[i] = find(p[i])
            return p[i]
        def union(i, j):
            p[find(i)] = find(j)
        for i in range(m):
            prev = None
            for j in range(n):
                if grid[i][j] == 1:
                    if prev == None: prev = i * n + j # be careful for zero is also false value, prev can be 0, so condition can't be "if prev: " 
                    else: union(prev, i * n + j)
        for j in range(n):
            prev = None
            for i in range(m):
                if grid[i][j] == 1:
                    if prev == None: prev = i * n + j
                    else: union(prev, i * n + j)
        counter = collections.Counter(find(i * n + j) for i in range(m) for j in range(n))
        return sum(v for k,v in counter.items() if v > 1)


    def countServers_2(self, grid: List[List[int]]) -> int:
        """ 
        Since the question only cares about # of all connected nodes, no need to figure out how many seperated connected components.
        You can simple count row by row and col by col to add all connected nodes into a set and the length of set will be the answer 
        """
        m, n = len(grid), len(grid[0])
        c_set = set()
        for i in range(m):
            row = [i * n + j for j in range(n) if grid[i][j] == 1]
            if len(row) > 1 : c_set.update(row)   # set update take iterable as parameters
        for j in range(n):
            col = [i * n + j for i in range(m) if grid[i][j] == 1]
            if len(col) > 1 : c_set.update(col)
        return len(c_set)

    def countServers(self, grid: List[List[int]]) -> int:
        """ 
        the position i, j connected iif (if and only if) the sum of i row  and sum j col added up >= 2
        """
        r_sum, c_sum = [sum(r) for r in grid], [*map(sum, zip(*grid))] # map zip return a iterator in python 3, and zip take unpacked list of list to make the col list
        return sum(r_sum[i] + c_sum[j] >= 2 and grid[i][j] == 1 for i in range(len(grid)) for j in range(len(grid[0])))

print(f'Answer is: {Solution().countServers([[1, 1], [1, 0]])}') #3