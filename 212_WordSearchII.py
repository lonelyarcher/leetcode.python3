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
        
        root = {}
        for w in words:
            cur = root
            for c in w:
                cur = cur.setdefault(c, {})
            cur['isWord'] = True

        #convert 2 dimension array to dict key as complex number
        #Python 2.7+ Dict Comprehensions
        nBoard = {
            i + j*1j: board[i][j]
            for i in range(len(board))
            for j in range(len(board[i]))
        }

        res = []

        def search(cur, p, path):
            if cur.pop('isWord', False):
                res.append(path)
            c = nBoard.get(p)
            if c in cur:
                nBoard[p] = None
                for k in range(4):
                    search(cur[c], p + 1j**k, path + c) #move the p 1 step to left, right, up and down
                nBoard[p] = c

        for p in nBoard:
            search(root, p, '')
        return res

        

words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
board = [["a","b"],["a","a"]]
s = Solution()
print(s.findWords(board, words))
words = ["aba","baa","bab","aaab","aaa","aaaa","aaba"]
board = []
print(s.findWords(board, words))