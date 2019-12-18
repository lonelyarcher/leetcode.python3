""" Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function hasNext() that returns True if and only if there exists a next combination.
 
Constraints:

1 <= combinationLength <= characters.length <= 15
There will be at most 10^4 function calls per test.
It's guaranteed that all calls of the function next are valid. """

class CombinationIterator:
    def __init__(self, cs: str, cl: int):
        def dfs (path, i): # combination 
            if cl == len(path): yield "".join(path)
            for j in range(i, len(cs)):
                path.append(cs[j])
                yield from dfs(path, j + 1) # delegate its operations to subgenerator, then the recursion will yield too
                path.pop()
        self.gen = dfs([], 0)
        self.buffer = next(self.gen)
    
    def next(self) -> str:
        ans = self.buffer
        self.buffer = next(self.gen, None)
        return ans
        
    def hasNext(self) -> bool:
        return self.buffer is not None

class CombinationIterator2:
    def __init__(self, cs: str, cl: int):
        def dfs (s, cl): # combination 
            if cl == len(s): yield s
            elif cl == 0: yield ""
            elif len(s) > cl:
                for tail in dfs(s[1:], cl - 1):
                    yield s[0] + tail
                for tail in dfs(s[1:], cl):
                    yield tail
        self.gen = dfs(cs, cl)
        self.buffer = next(self.gen)
    
    def next(self) -> str:
        ans = self.buffer
        self.buffer = next(self.gen, None)
        return ans
        
    def hasNext(self) -> bool:
        return self.buffer is not None
        

iterator = CombinationIterator2("abc", 2) # creates the iterator.

print(iterator.next()) # returns "ab"
print(iterator.hasNext()) # returns true
print(iterator.next()) # returns "ac"
print(iterator.hasNext()) # returns true
print(iterator.next()) # returns "bc"
print(iterator.hasNext()) #  returns false