""" We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average. """

import collections
from typing import List
class Solution_BFS:
    def minStickers(self, stickers: List[str], target: str) -> int:
        collections.Counter.__hash__ = lambda self: hash(tuple(sorted(self.items()))) #override __hash__ function of Counter
        t = collections.Counter(target)
        s = [collections.Counter(sticker) for sticker in stickers]
        step = 0
        seen = {t}
        q = collections.deque([t])
        while q:
            l = len(q)
            for _ in range(l):
                cnt = q.popleft()
                if sum(cnt.values()) == 0: return step
                for ss in s:
                    if list(cnt.keys())[-1] in ss: # Pruning, when use sticker to substract target, the order is irrelevant to result. 
                    #so we can first choose must substract one of character (here I pick the last one of counter keys) in target, then next character, the minimum step must be one of selections.
                        nt = cnt - ss
                        if sum(nt.values()) == 0: return step + 1
                        if nt not in seen:
                            q.append(nt)
                            seen.add(nt)
            step += 1
        return -1
import functools
class Solution_DFS:
    def minStickers(self, stickers: List[str], target: str) -> int:
        collections.Counter.__hash__ = lambda self: hash(tuple(sorted(self.items()))) #override __hash__ function of Counter
        t = collections.Counter(target)
        s = list(map(collections.Counter, stickers))
        if set(t).difference(*s): return -1 # set difference() = setA - setB, it can accept multiple arguments *
        @functools.lru_cache(None)
        def dfs (t):
            return 1 + min(dfs(t - cnt) for cnt in s if [*t][0] in cnt) if t else 0 #same pruning as BFS
        return dfs(t)

s = Solution_DFS()
print(s.minStickers(["these","guess","about","garden","him"], "atomher")) #3
print(s.minStickers(["with", "example", "science"], "thehat")) #3
print(s.minStickers(["notice", "possible"], "basicbasic")) #-1
