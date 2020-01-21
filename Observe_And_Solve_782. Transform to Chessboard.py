""" An N x N board contains only 0s and 1s. In each move, you can swap any 2 rows with each other, or any 2 columns with each other.

What is the minimum number of moves to transform the board into a "chessboard" - a board where no 0s and no 1s are 4-directionally adjacent? If the task is impossible, return -1.

Examples:
Input: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
Output: 2
Explanation:
One potential sequence of moves is shown below, from left to right:

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

The first move swaps the first and second column.
The second move swaps the second and third row.


Input: board = [[0, 1], [1, 0]]
Output: 0
Explanation:
Also note that the board with 0 in the top left corner,
01
10

is also a valid chessboard.

Input: board = [[1, 0], [1, 0]]
Output: -1
Explanation:
No matter what sequence of moves you make, you cannot end with a valid chessboard.
Note:

board will have the same number of rows and columns, a number in the range [2, 30].
board[i][j] will be only 0s or 1s. """

'''
first let careful observe the sample process
the target is chessboard, only two type of rows and columns: [1, 0, 1, 0, ...] and [0, 1, 0, 1, ...]
swap the rows and swap the columns are independent, when move rows, you only change order of all columns, same as move columns, you change order of all rows
so before swap, you should only have two types of rows and each position of two types have different 0 and 1
the mini-step to swap is to swap from original [0110] -> [1010] or [0101], if N is odd, [11100] -> [10101]
we can calculate the mask, then compare with original, the sum of diff /2 is min step to swap the rows
for the columns it is same to, we can put together with a loop to iterate rows and columns

'''


from typing import List
import collections
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        N = len(board)
        ans = 0
        for count in ((rows := collections.Counter(map(tuple, board))), (cols := collections.Counter(zip(*board)))):
            if len(count) != 2 or sorted(count.values()) != [N//2, (N + 1)//2]: return -1
            t1, t2 = count
            if not all(x^y for x, y in zip(t1, t2)): return -1
            mask = [t1.count(1) * 2 > N]
            for _ in range(1, N): mask.append(not mask[-1])
            if N % 2 == 1:
                ans += sum(x ^ y for x, y in zip(t1, mask)) // 2
            else:
                ans += min((diff := sum(x ^ y for x, y in zip(t1, mask)) // 2),  N//2 - diff)
        return ans



print(Solution().movesToChessboard([[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]])) # 2
print(Solution().movesToChessboard([[0, 1], [1, 0]])) # 0
print(Solution().movesToChessboard([[1, 0], [1, 0]])) # -1