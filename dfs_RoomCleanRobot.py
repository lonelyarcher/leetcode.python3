'''
已知扫地机器人有move(), turn_left(k), turn_right(k), clean()方法，机器人能面向东
南西北四个方向，move是按当前方向移动一格，如果不能移动返回false;
turn_left(k), turn_right(k)是旋转k*90度; 房间里可能有障碍物，机器人并不知道房间
的布局，设计算法让扫地机器人清扫房间（走完房间每一格）。
这道题主要是要把题目给抽象出来。简历坐标系，然后把调用API的函数给拉出来

单独写。这样的话，题目本身其实就是一个dfs遍历matrix的题目了。
# move(), turn_left(k), turn_right(k), clean()
'''
class Robot(object):
    
    '''
    题目隐藏了Robot的一种重要参数 abs direction, 即为当前robot朝那个方向:
    我们定位为 0 x轴向右， j+1
              1 y轴向下， i+1
              2 x轴向左， j-1
              3 y轴向上， i-1
    '''
    mov_d = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)} 
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
        self.cleanable = len([ 1 for i in range(len(room)) for j in range(len(room[0])) if room[i][j] == 0 ])
        self.dfs()       
        if len(self.visited) < self.cleanable:    
            self.robot.turn_right(1)
            self.visited.clear()
            print("couldn't move from the initial position, adjust the direction by right to ({},{},{})".format(self.robot.x, self.robot.y, self.robot.dir))
            self.dfs()

    def dfs(self):
        if 0 <= self.robot.x < len(room) and 0 <= self.robot.y < len(room[0]) and room[self.robot.x][self.robot.y] == 0:
            self.robot.clean()
            self.visited.add((self.robot.x, self.robot.y))
            if len(self.visited) == self.cleanable:
                print("Successfully clean the room, then return to the initail position")
                return
            
            for d in [-1, 0, 1]:
                self.robot.mov_dir(d)
                print("move to ({}, {}, {})".format(self.robot.x, self.robot.y, self.robot.dir))
                self.dfs()
                self.robot.back_from(d)
                print("back to ({}, {}, {})".format(self.robot.x, self.robot.y, self.robot.dir))

      

# test
room = [
[0, 0, 0, 1],
[1, 0, 1, 1],
[1, 0, 1, 1]
]
robot = Robot(0, 2, 0)
print("initial robot ({},{},{})".format(robot.x, robot.y, robot.dir))
s = Solution()
s.robotClean(robot, room)

        

