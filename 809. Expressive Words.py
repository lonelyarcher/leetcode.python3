""" Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", 
we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".

For some given string S, a query word is stretchy if it can be made to be equal to S by any number of applications of the following extension operation: 
choose a group consisting of characters c, and add some number of characters c to the group so that the size of the group is 3 or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo", 
but we cannot get "helloo" since the group "oo" has size less than 3.  
Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  
If S = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations: 
query = "hello" -> "hellooo" -> "helllllooo" = S.

Given a list of query words, return the number of words that are stretchy. 

 

Example:
Input: 
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation: 
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 

Notes:

0 <= len(S) <= 100.
0 <= len(words) <= 100.
0 <= len(words[i]) <= 100.
S and all words in words consist only of lowercase letters """


from typing import List
import re
import itertools
class Solution:
    '''generate all possible stretchy string set '''
    def expressiveWords(self, S: str, words: List[str]) -> int:
        wset = {S}
        ms = [*re.finditer(r'([a-z])\1{2,}', S)] #find any repeating characters more than 3
        def dfs(path, i):
            if i == len(ms):
                str = S
                for m, sub in zip(ms[::-1], path[::-1]):
                    str = str[:m.start()] + sub + str[m.end():]
                wset.add(str)
                return
            start, end = ms[i].start(), ms[i].end()
            for j in range(1, end - start):
                path.append(S[start:start + j])
                dfs(path, i + 1)
                path.pop()
        dfs([], 0)
        #print(wset)
        return len(wset & set(words))

    '''compare the count array, 
    "heeellooo" => key: [h, e, l, o], count: [1, 3, 2, 3]
    "hello"  => key: [h, e, l, 0],    count: [1, 1, 2, 1]
    if key1 == key2, then all(count1[i] > count2[i] and (count1[i] >= 3 or count1[i] == count2[i]) for i in range(len(count)))
    '''
    def expressiveWords(self, S: str, words: List[str]) -> int:
        def helper(s):
            k, count = [s[0]], []
            pre, cnt = s[0], 0
            for c in s:
                if c == pre: 
                    cnt += 1
                else:
                    k.append(c)
                    count.append(cnt)
                    cnt = 1
                    pre = c
            count.append(cnt)
            return k, count

        def helper2(s):
            return zip(*((k, len([*g_list])) for k, g_list in itertools.groupby(s)))
        sk, s_count = helper2(S) 
        ans = 0
        for w in words:
            wk, w_count = helper2(w)
            if wk != sk: continue
            if all(c1 > c2 and c1 >= 3 or c1 == c2 for c1, c2 in zip(s_count, w_count)): ans += 1
        return ans

print(Solution().expressiveWords(S = "heeellooo", words = ["hello", "hi", "helo"])) # 1