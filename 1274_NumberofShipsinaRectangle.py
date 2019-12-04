""" (This problem is an interactive problem.)

On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if 
there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  
It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  
Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example :

Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.
 
Constraints:

On the input ships is only given to initialize the map internally. You must solve this problem "blindfolded". 
In other words, you must find the answer using the given hasShips API, without knowing the ships position.
0 <= bottomLeft[0] <= topRight[0] <= 1000
0 <= bottomLeft[1] <= topRight[1] <= 1000 """

# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
class Sea(object):
   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
       pass

class Point(object):
	def __init__(self, x: int, y: int):
		self.x = x
		self.y = y

""" Quaternary search, rectangle divided into 4, take (x1 + x2)//2, (y1 + y2)//2
take middle point will fall to lower point i when the difference decrease to i and i + 1, (i + i + 1) //2 = i (lower i)
so to avoid the points shared between quaternary rectangle, divide as (mid, bottomLeft), ((midX + 1, midY + 1) topRight), ...
Until divide into a point, topRight == bottomLeft, call hasShips, if has then count = 1
if topRight < bottomLeft, it is invalid rectangle, return 0
 """
class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        x1, y1, x2, y2 = topRight.x, topRight.y, bottomLeft.x, bottomLeft.y
        if x1 < x2 or y1 < y2 or not sea.hasShips(topRight, bottomLeft): return 0
        if x1 == x2 and y1 == y2: return 1 
        
        mx, my = (x1 + x2)//2, (y1 + y2)//2
        return (self.countShips(sea, Point(mx, y1), Point(x2, my + 1)) 
            + self.countShips(sea, topRight, Point(mx + 1, my + 1)) 
            + self.countShips(sea, Point(x1, my), Point(mx + 1, y2)) 
            + self.countShips(sea, Point(mx, my), bottomLeft) )
