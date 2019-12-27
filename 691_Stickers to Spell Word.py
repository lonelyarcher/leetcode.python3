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

'''
based on the input size, it should be a search question, but can be optimized by backtracking
'''

import collections
from typing import List
class Solution_ListAsState:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        def str2arr(s):
            ans = [0] * 26
            for ch in s:
                ans[ord(ch) - 97] += 1
            return ans
        def substract(a, b):
            return [max(0, x - y) for x, y in zip(a, b)] 
        t = str2arr(target)
        s = [str2arr(sticker) for sticker in stickers]
        step = 0
        seen = {tuple(t)}
        q = collections.deque([t])
        while q:
            l = len(q)
            for _ in range(l):
                arr = q.popleft()
                if sum(arr) == 0: return step
                for ss in s:
                    nt = substract(arr, ss)
                    if sum(nt) == 0: return step + 1
                    if tuple(nt) not in seen:
                        q.append(nt)
                        seen.add(tuple(nt))
            step += 1
        return -1

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        t = collections.Counter(target)
        s = [collections.Counter(sticker) for sticker in stickers]
        step = 0
        seen = {tuple(sorted(t.items()))}
        q = collections.deque([t])
        while q:
            l = len(q)
            for _ in range(l):
                cnt = q.popleft()
                if sum(cnt.values()) == 0: return step
                for ss in s:
                    nt = cnt - ss
                    if sum(nt.values()) == 0: return step + 1
                    if (hash := tuple(sorted(nt.items()))) not in seen:
                        q.append(nt)
                        seen.add(hash)
            step += 1
        return -1


print(Solution().minStickers(["these","guess","about","garden","him"], "atomher")) #3
print(Solution().minStickers(["with", "example", "science"], "thehat")) #3
print(Solution().minStickers(["notice", "possible"], "basicbasic")) #-1
