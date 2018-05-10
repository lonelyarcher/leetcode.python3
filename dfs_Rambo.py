'''
已知扫地机器人有move(), turn_left(k), turn_right(k), clean()方法，机器人能面向东
南西北四个方向，move是按当前方向移动一格，如果不能移动返回false;
turn_left(k), turn_right(k)是旋转k*90度; 房间里可能有障碍物，机器人并不知道房间
的布局，设计算法让扫地机器人清扫房间（走完房间每一格）。
这道题主要是要把题目给抽象出来。简历坐标系，然后把调用API的函数给拉出来
单独写。这样的话，题目本身其实就是一个dfs遍历matrix的题目了。
# move(), turn_left(k), turn_right(k), clean()
'''
import copy
class Robot(object):
    mov_d = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
    def mov(self):
        self.x += Robot.mov_d[self.dir][0]
        self.y += Robot.mov_d[self.dir][1]
    def turn_right(self, k):
        self.dir = (self.dir + k) % 4
    def turn_left(self, k):
        self.dir = (self.dir - k) % 4
    def clean(self):
        print("clean ({}, {})".format(self.x, self.y))
    
    def try_mov(self, d): # d: 'forward': 0, 'left': -1, 'right': 1
        dummy = copy.copy(self)
        dummy.mov_dir(d)
        return (dummy.x, dummy.y)

    def mov_dir(self, d): # d: 'forward': 0, 'left': -1, 'right': 1       
        if d == 0:
            self.mov()
        elif d == -1:
            self.turn_left(1)
            self.mov()
        elif d == 1:
            self.turn_right(1)
            self.mov()
    
    def back(self):
        self.turn_left(2)
        self.mov()
        self.turn_left(2)
    
    def back_from(self, d): # d: 'forward': 0, 'left': -1, 'right': 1  
        if d == 0:
            self.back()
        elif d == -1:
            self.back()
            self.turn_right(1)
        elif d == 1:
            self.back()
            self.turn_left(1)

    
class Solution(object):

    def robotClean(self, robot, room):
        self.robot = robot
        self.room = room
        self.visited = set()
        self.dfs()

    def dfs(self):
        if len(self.visited) == len([ 1 for i in range(room) for j in range(room[0]) if room[i][j] == 0 ]):
            return "Successfully clean the room"
        self.robot.clean()
        self.visited.add((self.robot.x, self.robot.y))
        
        for d in [-1, 0, 1]:
            (nx, ny) = self.robot.try_mov(d)
            if 0 <= nx < len(room) and 0 <= ny < len(room[0]) and room[nx][ny] == 0:
                self.robot.mov_dir(d)
                self.dfs()
                self.robot.back_from(d)

      

# test
room = [
[0, 0, 0, 1],
[1, 0, 1, 1],
[1, 0, 1, 1]
]
robot = Robot(0, 0, 0)
s = Solution()
print(s.robotClean(robot, room))

        

