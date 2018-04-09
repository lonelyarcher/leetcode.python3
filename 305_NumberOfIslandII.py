class UnionFind():
    def __init__(self):
        self.cnt = 0
        self.dic = {}
    
    def add(self, i, j):
        if (i, j) not in self.dic:
            self.dic[(i, j)] = (i, j)
            self.cnt += 1
    
    def find(self, p):
        while p != self.dic[p]:
            self.dic[p] = self.dic[self.dic[p]]
            p = self.dic[p]
        return p

    def unite(self, p, q):
        p_anc, q_anc = self.find(p), self.find(q)
        if p_anc == q_anc:
            return
        else:
            self.cnt -= 1
            self.dic[p_anc] = q_anc

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int] """
        uf = UnionFind()
        res = []

        for i, j in positions:
            uf.add(i, j)
            for d, p in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                x, y = i+d, j+p
                if (x, y) in uf.dic:
                    uf.unite((i, j), (x, y))
            res.append(uf.cnt)
        return res

p = [[0,1],[1,2],[2,1],[1,0],[0,2],[0,0],[1,1]]
s = Solution()
print(s.numIslands2(3, 3, p))
