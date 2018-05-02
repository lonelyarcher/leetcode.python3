'''
find out wether you can find treasure in rooms
room connect room (neighbors list)
room has key to connect two rooms. (key: (room1, room2)) 
dfs, recursion will not work, because it has two factors: room connections and keys
so need two stacks (rooms and keys) to do while loop for dfs. 
First pop the rooms, if no room available, pop keys to add rooms.
If both of stack empty, then ends. 
visited set to record visited rooms
'''

class Room:
    def __init__(self):
        self.treasure = False
        self.key = None
        self.neighbors = []

class Solution:
    def canFind(self, room):
        rooms = [room]
        visited = set()
        keys = []
        while rooms or keys:
            if rooms:
                cur = rooms.pop()
                visited.add(cur)
                if cur.treasure: return True
                if cur.key: keys.append(cur.key)
                for child in cur.neighbors:
                    if child not in visited:
                        rooms.append(child)
            if keys:
                a, b = keys.pop()
                if a in visited and b not in visited:
                    rooms.append(b)
                elif b in visited and a not in visited:
                    rooms.append(a)
        return False

        

# test
a = Room()
b = Room()
c = Room()
c.treasure = True
a.neighbors = [b]
b.key = (a, c)
s = Solution()
print(s.canFind(a))


        