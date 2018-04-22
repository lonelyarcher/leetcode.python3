'''
Implement a auto fill class. It will take a word dictionary for init. then it will auto fill
the word you are entered. You can understand this by looking at my code.
'''
class Solution():
    def __init__(self, words): # dict is not hashable because only immutable object could be hashed in Python
        self.root = {}
        self.rank = {w:0 for w in words}
        for w in words:
            cur = self.root
            for c in w:
                cur = cur.setdefault(c, {})
            cur['value'] = w
    def get_words(self, str):
        cur = self.root
        for c in str:
            if c not in cur: return []
            cur = cur[c]
        suggestion = []
        self.dfs(cur, suggestion)
        return sorted(suggestion, key=lambda x: (-self.rank[x], x))

    def dfs(self, cur, suggestion):
        if 'value' in cur: 
            suggestion.append(cur['value'])
        for c in cur:
            if c != 'value': self.dfs(cur[c], suggestion)

    def pick(self, str):
        self.rank[str] += 1

            

#test
words = ['app', 'apple', 'application', 'appeal', 'ape', 'approve', 'apply', 'applicant', 'age', 'add', 'average', 'boy', 'bat']
s = Solution(words)
# first we get suggestuon for prefix ap
print(s.get_words('ap'))
# then we get suggestion for prefix b
print(s.get_words('b'))
# we decided to pick bat as our input
s.pick('bat')
# next time b will be ranked higher
print(s.get_words('b'))
s.pick('appeal')
print(s.get_words('a'))