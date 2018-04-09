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