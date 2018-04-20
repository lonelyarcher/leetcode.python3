'''
1.买水果
public static int checkWinner (List<List<String>> codeList, List
<String> shoppingCart) {}
说的是小明要帮公司买水果，给了一个codeList， 里面装的是他买的水果，给了一个
shoppingCart里面装的是target水果，目标是检查codelist里的水果顺序是否和s
hoppingCart里的顺序匹配。
注意的是只有codelist中的所有链表的item之后加起来小于等于shoppingcart里it
em之和才可能返回1。 另外在codelist中有可能出现item时 "anything"， 它可
以和任意的水果匹配。
Ex1:
codelist:
[
[apple, apple],
[orange, banana, orange]
].
shoppingCart: [orange, apple, apple, orange, banana, orange].
return 1, 因为codelist里的顺序和shoppingcart里除了第一个orange之后的水
果顺序匹配.
Ex2:
codelist:
[
[orange, banana, orange]，
[apple, apple]
]
shoppingCart: [orange, apple, apple, orange, banana, orange]
return 0, 因为codeList里的顺序和shoppingcart没法匹配。
Ex3: .
codelist:
[
[apple, apple],
[orange, banana, orange],
[pear, orange, grape].
].
shoppingCart: [orange, apple, apple, orange, banana, orange, pea
r, grape]
return 0, 因为codelist里最后一个[pear, orange, grape]中的orange没法
和shoppingcart里的水果匹配。
Ex4:
codeList:
[
[apple, apple],
[orange, anything, orange]
]
shoppingCart:
[orange, apple, apple, orange, mango, orange]
return 1。
'''

import itertools
class Solution():
    # we can flat the list<list> then double point go through to find match or not
    def buyFruit_flat(self, codesList, shoppingCart):
        codes = list(itertools.chain.from_iterable(codesList))
        codes = [c for c in sublist for sublist in codesList]
        print(codes)
        i, j = 0, 0
        m, n = len(codes), len(shoppingCart)
        def isMatch(c, s):
            if c == 'anything' or c == s: return True
            return False
        while i < m and j < n:
            if isMatch(codes[i], shoppingCart[j]):
                i += 1
            else:
                i = 0
            j += 1
        return i == m

    # best solution, loop the shoppingCart which the template, if find pattern (codesList) match to end, then return True
    # to iterate the list of list, use two dimension point i, j. when matching, move forward j, if j reach end of sublist codesList[i], move I and j = 0
    def buyFruit(self, codesList, shoppingCart):
        i, j = 0, 0
        def isMatch(c, s):
            if c == 'anything' or c == s: return True
            else: return False
        for sh in shoppingCart:
            if isMatch(codesList[i][j], sh):
                j += 1
                if j == len(codesList[i]):
                    i += 1
                    j = 0
                    if i == len(codesList): return True
            else:
                i, j = 0, 0
        return False
codesList = [
['apple', 'apple'],
['orange', 'banana', 'orange']
]
shoppingCart = ['orange', 'apple', 'apple', 'orange', 'banana', 'orange']
print(Solution().buyFruit(codesList, shoppingCart))

codesList = [
['orange', 'banana', 'orange'],
['apple', 'apple']
]
shoppingCart = ['orange', 'apple', 'apple', 'orange', 'banana', 'orange']
print(Solution().buyFruit(codesList, shoppingCart))
codesList = [
['apple', 'apple'],
['orange', 'banana', 'orange'],
['pear', 'orange', 'grape']
]
shoppingCart = ['orange', 'apple', 'apple', 'orange', 'banana', 'orange', 'pear', 'grape']
print(Solution().buyFruit(codesList, shoppingCart))
codesList = [
['apple', 'apple'],
['orange', 'anything', 'orange']
]
shoppingCart = ['orange', 'apple', 'apple', 'orange', 'mango', 'orange']
print(Solution().buyFruit(codesList, shoppingCart))