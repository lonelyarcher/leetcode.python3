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
# we can flat the list<list> then double point go through to find match or not
import itertools
class Solution():
    def buyFruit(self, codeList, shoppingCart):
        codes = itertools.chain(codeList)
        i, j = 0, 0
        m, n = len(codes), len(shoppingCart)
        def isMatch(c, s):
            if c == 'anything' or c == s: return True
            return false
        while i < m and j < n:
            if isMatch(codes[i], shoppingCart[j]):
                j += 1
            else:
                j = 0
            i += 1
        return j == n
print(Solution.buyFruit())