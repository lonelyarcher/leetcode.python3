# Generate a playlist from list of songs which no same song in adjacent sequence
class Solution(object):
    def playList(self, songs, target):
        if not songs or not target: return None
        res = []
        for song in songs:
            self.dfs([song], songs, target - 1, res)
        return res
    def dfs(self, cur, songs, remain, res):
        if remain == 0:
            res.append(cur[:])
        else:
            for song in [ s for s in songs if s != cur[-1] ]:
                cur.append(song)
                self.dfs(cur, songs, remain - 1, res)
                cur.pop()

# test
songs = [0,1,2] 
target = 4
print(Solution().playList(songs, target))