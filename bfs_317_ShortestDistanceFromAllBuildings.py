'''
You want to build a house on an empty land which reaches all buildings in the
shortest amount of distance. You can only move up, down, left and right. You are
given a 2D grid of values 0, 1 or 2, where:
Each 0 marks an empty land which you can pass by freely. Each 1 marks a
building which you cannot pass through. Each 2 marks an obstacle which you
cannot pass through. For example, given three buildings at (0,0), (0,4), (2,2), and
an obstacle at (0,2):
1 - 0 - 2 - 0 - 1
| | | | |
0 - 0 - 0 - 0 - 0
| | | | |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance
of 3+3+1=7 is minimal. So return 7.
https://leetcode.com/problems/shortest-distance-from-all-buildings/
思路： 我们用一个matrix来记录能到达i,j位置的building数和距离的和。然后对每一
个grid值为1的点进行bfs就行了。
'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
