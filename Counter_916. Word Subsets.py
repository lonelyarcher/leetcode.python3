""" We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a. 

Return a list of all universal words in A.  You can return the words in any order.


1 <= A.length, B.length <= 10000
1 <= A[i].length, B[i].length <= 10
A[i] and B[i] consist only of lowercase letters.
All words in A[i] are unique: there isn't i != j with A[i] == A[j]. """

from collections import Counter
from functools import reduce
from typing import List
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        bc = reduce(lambda a, b: a|b, (Counter(b) for b in B))
        return [e for e in A if Counter(e) & bc == bc]

print(Solution().wordSubsets(A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"])) #["facebook","leetcode"]