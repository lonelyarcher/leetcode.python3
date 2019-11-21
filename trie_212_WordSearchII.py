'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
'''
class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0: return []
        m, n = len(board), len(board[0])
        root = {}
        for w in words:
            cur = root
            for c in w:
                cur = cur.setdefault(c, {})
            cur['isWord'] = True

        #convert 2 dimension array to dict key as complex number
        #Python 2.7+ Dict Comprehensions
        dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        res = []
        def search(cur, p, path):
            i, j = p
            if cur.pop('isWord', False):
                res.append(path)
            c = board[i][j]
            if c in cur:
                board[i][j] = None
                for d in dir:
                    ni, nj = i + d[0], j + d[1]
                    if ni >= 0 and ni < m and nj >= j and nj < n: 
                        if c not in cur:
                            print(c)
                        search(cur[c], (ni, nj), path + c) #move the p 1 step to left, right, up and down
                board[i][j] = c

        for i in range(m):
            for j in range(n):
                search(root, (i, j), '')
        return res

        

words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
board = [["a","b"],["a","a"]]
s = Solution()
print(s.findWords(board, words))
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
board = []
print(s.findWords(board, words))