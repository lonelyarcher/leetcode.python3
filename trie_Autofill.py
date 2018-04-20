'''
Implement a auto fill class. It will take a word dictionary for init. then it will auto fill
the word you are entered. You can understand this by looking at my code.
'''
class Solution():
    pass


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