'''
given a bag of chars, and a dictionary contains with many words, find list of
maximum length word which can be generated from the bag of chars respectively.
字符集中的字符不一定全用上。
bag may contain duplicate characters.The char in bag cannot be reused. bag
{a,p,l,e} cannot generate word 'apple'.
case 2: bag of chars
{'a', 'p', 'p', 'l', 'e', 'o'}
dict
{'apple', 'people'}
return
{'apple'}
because people need 2 char 'e', there is only 1 'e' in the bag.
'''
from collections import Counter
class Solution():
    def findLongest(self, bag, words):
        """
        :type bag: List[char]
        :type words: List[str]
        :rtype: str
        """
        bag = Counter(bag)
        maxL = ""        
        for w in words:
            valid = True
            wcounter = Counter(w)
            for k in wcounter:
                #print(k, list(g))
                if k not in bag or wcounter[k] > bag[k]: valid = False
            if valid and len(w) > len(maxL):
                maxL = w
        return maxL

#test
bag = ['u','b','e','r','d']
words = ['uber', 'red']
print(Solution().findLongest(bag, words))
bag = ['a','p','p','l','e','o']
words = {'apple', 'people'}
print(Solution().findLongest(bag, words))
bag = ['i','n','b','o','x','d','r','a','f','t','m','r','e']
words = {'inbox', 'draft', 'more'}
print(Solution().findLongest(bag, words))               
