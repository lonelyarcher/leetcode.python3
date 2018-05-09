'''
Tom is chasing jerry in a maze. He needs to eat all Cheeses in the maze, then
only then he will be able to reach Jerry. You have to find smallest path that TOM
should take to eat all Cheeses and reach Jerry. TOM can only run straight – left,
right, top and down. Input : Tom Position (0,0) Jerry Position (3,3) we use 2 to
represent cheese in maze, 1 represent wall.
matrix = [
[T,0,1,1],
[2,0,0,1],
[2,0,0,0],
[2,2,2,J]
]
思路：暴力DFS就可以了。DFS的中止条件是，走到了jerry那里并且吃光了所有
cheese。
不过我们可以通过剪枝来优化。因为我们最后需要输出的steps,所以如果我们存当
前最小的steps，只要超过这个steps我们就没必要再往下dfs了。需要注意的是，因
为路径可以重复走（因为有可能cheese在一条死路里，必须原路返回， 十字路口可能要访问6次），所以我们
要用一个set来存已经吃过的cheese，再走到这个cheese的时候我们就不+1 cheese了。
'''
from math import inf
class Solution(object):
    def mazeGame(self, start, end, matrix):
        if not matrix or not matrix[0]: return 0
        maze = {i + 1j*j: [matrix[i][j], 0] for i in range(len(matrix)) for j in range(len(matrix[0]))}
        cheese = sum([1 for i in maze if maze[i][0] == 2])
        minStep = 100
        def dfs(cur, c, step):
            nonlocal minStep
            if step >= minStep or maze[cur][0] == 1 or maze[cur][1] > 6: return 
            maze[cur][1] += 1
            if maze[cur][0] == 2 and maze[cur][1] == 1: c += 1
            if cur == end[0] + 1j*end[1] and c == cheese: minStep = step          
            for i in range(4):
                nex = cur + 1j**i
                if nex in maze: dfs(nex, c, step + 1)
            maze[cur][1] -= 1
        dfs(start[0] + 1j*start[1], 0, 0)
        return minStep

#test
matrix = [
[0,0,1,1],
[2,0,0,1],
[2,2,0,0],
[2,2,2,0]
]
start = [0,0]
end = [3,3]

print(Solution().mazeGame(start, end, matrix))

