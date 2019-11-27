""" 
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col 
"""
from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m = len(matrix)
        self.n = 0 if self.m == 0 else len(matrix[0])
        self.bit = [[0] * (self.n + 1) for i in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.updateBit(i + 1, j + 1, self.matrix[i][j])
        print("\n".join(f'[{",".join(str(self.bit[i][j]) for j in range(self.n + 1))}]' for i in range(self.m + 1)))
    
    def update(self, row: int, col: int, val: int) -> None:
        
        delta = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.updateBit(row + 1, col + 1, delta)

    def updateBit(self, r, c, delta):
        i = r
        while i < self.m + 1:
            j = c
            while j < self.n + 1:
                self.bit[i][j] += delta
                j += j & (-j)
            i += i & (-i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.query(row2 + 1, col2 + 1) - self.query(row1, col2 + 1) - self.query(row2 + 1, col1) + self.query(row1, col1)

    def query(self, r, c):
        sum = 0
        i = r
        while i > 0: 
            j = c
            while j > 0:
               sum += self.bit[i][j]
               j -= j & (-j)
            i -= i & (-i)
        return sum 
        


m = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
so = NumMatrix(m)
print(so.sumRegion(2, 1, 4, 3)) # 8
so.update(3, 2, 2)
print(so.sumRegion(2, 1, 4, 3)) # 10