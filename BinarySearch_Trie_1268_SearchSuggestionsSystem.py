""" Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 

Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
Example 2:

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
Example 3:

Input: products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output: [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
Example 4:

Input: products = ["havana"], searchWord = "tatiana"
Output: [[],[],[],[],[],[],[]]
 

Constraints:

1 <= products.length <= 1000
1 <= Σ products[i].length <= 2 * 10^4
All characters of products[i] are lower-case English letters.
1 <= searchWord.length <= 1000
All characters of searchWord are lower-case English letters. """
from typing import List
import bisect
class Solution:
    def suggestedProducts_Trie(self, products: List[str], searchWord: str) -> List[List[str]]:
        """ Trie to implements prefix suggestions, 
        each node save the list of word passing this node """
        root = {}
        for w in products:
            p = root
            for c in w:
                p = p.setdefault(c, {})
                p.setdefault('list', []).append(w)
                p['list'] = sorted(p['list'])[:3]
        ans = []
        p = root        
        found = True   
        for c in searchWord:
            suggestions = []
            if c in p and found: 
                p = p[c]
                suggestions = p['list']
            else: found = False
            ans.append(suggestions)
        return ans

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        """ 
        Binary Search
        Sort the products, binary search the searchWord, find the index begin with this prefix and end of this prefix
        """
        products.sort()
        ans = []
        for i in range(len(searchWord)):
            suggestions = []
            prefix = searchWord[:i + 1]
            j = bisect.bisect_left(products, prefix) #bisect.bisect_right is default, insert_left is find first GE, insert_right is find first GT
            while j < len(products) and len(suggestions) < 3 and products[j].startswith(prefix): 
                suggestions.append(products[j])
                j += 1
            ans.append(suggestions)
        return ans
print(Solution().suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"))


