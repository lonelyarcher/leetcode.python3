'''
Given n pairs of parentheses, write a function to generate all combinations of wellformed
parentheses.
For example, given n = 3, a solution set is:
[
"((()))",
"(()())",
"(())()",
"()(())",
"()()()"
]
'''
class Solution(object):
    # dfs
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        def dfs(str, left, right):
            if left < right or left > n or right > n:
                return
            elif left == n and right == n:
                res.append(str)
            else:
                dfs(str + "(", left + 1, right)
                dfs(str + ")", left, right + 1)
        dfs("", 0, 0)
        return res

# test
print(Solution().generateParenthesis(3))