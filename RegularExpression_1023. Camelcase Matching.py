""" A query word matches a given pattern if we can insert lowercase letters to the pattern word so that it equals the query. (We may insert each character at any position, and may insert 0 characters.)

Given a list of queries, and a pattern, return an answer list of booleans, where answer[i] is true if and only if queries[i] matches the pattern.

 

Example 1:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]
Explanation: 
"FooBar" can be generated like this "F" + "oo" + "B" + "ar".
"FootBall" can be generated like this "F" + "oot" + "B" + "all".
"FrameBuffer" can be generated like this "F" + "rame" + "B" + "uffer".
Example 2:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
Output: [true,false,true,false,false]
Explanation: 
"FooBar" can be generated like this "Fo" + "o" + "Ba" + "r".
"FootBall" can be generated like this "Fo" + "ot" + "Ba" + "ll".
Example 3:

Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
Output: [false,true,false,false,false]
Explanation: 
"FooBarTest" can be generated like this "Fo" + "o" + "Ba" + "r" + "T" + "est".
 

Note:

1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
All strings consists only of lower and upper case English letters. """

from typing import List
import re
class Solution:
    def camelMatch_re(self, queries: List[str], pattern: str) -> List[bool]:
        return [bool(re.fullmatch(rf'[a-z]*{"[a-z]*".join(pattern)}[a-z]*', q)) for q in queries]

# two pointer, while loop only one action per iterate, prefer not: while: while: which you need to judge twice
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(q):
            pq, pp = 0, 0
            while pq < len(q):
                if pp == len(pattern) or q[pq] != pattern[pp]:
                    if q[pq].isupper(): return False
                else:
                    pp += 1
                pq += 1
            return pp == len(pattern)
        return [check(q) for q in queries]
            
print(Solution().camelMatch_re(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB")) # [true,false,true,true,false]
print(Solution().camelMatch_re(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa")) # [true,false,true,false,false]
print(Solution().camelMatch_re(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT")) # [false,true,false,false,false]
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB")) # [true,false,true,true,false]
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa")) # [true,false,true,false,false]
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT")) # [false,true,false,false,false]
