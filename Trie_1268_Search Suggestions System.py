""" Given an array of strings products and a string searchWord. 
We want to design a system that suggests at most three product names from products after each character of searchWord is typed.
Suggested products should have common prefix with the searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

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
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = {}
        for w in products:
            p = root
            for c in w:
                p = p.setdefault(c, {})
            p['value'] = w
        ans = []
        p = root
        def dfs(p, suggestions):
            if 'value' in p: suggestions.append(p['value'])
            for c in p:
                if c != "value": dfs(p[c], suggestions)
        
        found = True   
        for c in searchWord:
            suggestions = []
            if c in p and found: 
                p = p[c]
                dfs(p, suggestions)
            else: found = False 
            ans.append(sorted(suggestions)[0:3])
        return ans

# save the suggestions list in every trie node
    def suggestedProducts2(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = {}
        for w in products:
            p = root
            for c in w:
                p = p.setdefault(c, {})
                p['list'] = p.get('list', [])
                p['list'].append(w)
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

print(Solution().suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")) #