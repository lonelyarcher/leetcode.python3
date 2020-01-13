""" There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

0 <= N <= 10^5
String dominoes contains only 'L', 'R' and '.' """

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        s, preR = 0, -1
        ans = list(dominoes)
        for i, c in enumerate(dominoes):
            if c == 'R':
                preR = i
            elif c == '.':
                if preR > -1: 
                    ans[i] = 'R'
            else:
                if preR == -1:
                    for j in range(s, i):
                        ans[j] = 'L'       
                else:
                    mid = (preR + i) // 2
                    for j in range(mid + 1, i):
                        ans[j] = 'L'
                    if (preR + i) % 2 == 0:
                        ans[mid] = '.'
                s, preR = i + 1, -1
        return ''.join(ans)


print(Solution().pushDominoes(".L.R...LR..L..")) # Output: "LL.RR.LLRRLL.."
print(Solution().pushDominoes("RR.L")) # Output: "RR.L"