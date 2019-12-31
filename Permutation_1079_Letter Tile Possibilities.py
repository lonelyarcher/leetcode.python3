""" You have a set of tiles, where each tile has one letter tiles[i] printed on it.  Return the number of possible non-empty sequences of letters you can make.

 

Example 1:

Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: "AAABBC"
Output: 188
 

Note:

1 <= tiles.length <= 7
tiles consists of uppercase English letters. """

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        A = sorted(tiles)
        seen = [0] * len(A)
        def dfs(path, i):
            ans = 1
            for j in range(len(A)):
                if seen[j] or (j > 0 and A[j] == A[j - 1] and not seen[j - 1]): continue
                seen[j] = 1
                ans += dfs(path + A[j], j + 1)
                seen[j] = 0
            return ans
        return dfs("", 0) - 1