'''
已知扫地机器人有move(), turn_left(k), turn_right(k), clean()方法，机器人能面向东
南西北四个方向，move是按当前方向移动一格，如果不能移动返回false;
turn_left(k), turn_right(k)是旋转k*90度; 房间里可能有障碍物，机器人并不知道房间
的布局，设计算法让扫地机器人清扫房间（走完房间每一格）。
这道题主要是要把题目给抽象出来。简历坐标系，然后把调用API的函数给拉出来
单独写。这样的话，题目本身其实就是一个dfs遍历matrix的题目了。
# move(), turn_left(k), turn_right(k), clean()
'''
class robot(object):
    def __init__(self, x, y, dir, room):
        self.x = x
        self.y = y
        self.dir = dir
        self.room = room
    def mov(self):
        pass
    def turnRight(self, k):
        pass
    def turnLeft(self, k):
        pass
    def clean(self):
        pass

    def back(self):
        self.turnRight(2)
        self.mov()
        self.turnRight(2)
    


    def robotClean(self):
        self.visited = set()
        self.dfs()

    def dfs(self):
        if len(self.visited) == len(self.room) * len(self.room[0]):
            return
        robot.clean()
        self.visited.add((x, y))
        
        robot.move()
        self.dfs(robot, room)
        robot.back()

        turnRight()
        self.dif(robot, room)
        

