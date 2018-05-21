'''
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, /, (, ) operators
and empty spaces . The integer division should truncate toward zero.
You may assume that the given expression is always valid.
思路：用stack, 一个存数，一个存operation。遇到符号，就检查上一个operation是
不是*或者/是的话就先算。遇到反括号‘）’,就一直算到遇到‘（’为止。最后loop完s，
nums中只剩数字，ops中只剩+ or -。一个一个op地pop出来，然后算好push回去就
行了。
'''
# two stack for +-*/(), one stack for +-*/
# always handle the if digit, then else first handle get number for digit end.
# then anything else like ()+-/*, ( for push the operator to the stack, ) pop

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: ints
        """
        s = s + " "  # add the fake end to finish last number
        num, nums, ops = 0, [0], []
        
        def calc_one():
            y, x, op = nums.pop(), nums.pop(), ops.pop()
            if op == '+': nums.append(x + y)
            elif op == '-': nums.append(x - y)
            elif op == '*': nums.append(x * y)
            else: nums.append(x // y)

        for i in range(len(s)):
            if s[i] in '1234567890':                    # is number
                num = num * 10 + int(s[i])
            else:
                if i > 0 and s[i-1] in '123456789':     # end of numbers
                    nums.append(num)
                    num = 0
                if s[i] == ')':                         # is (
                    while ops[-1] != '(': calc_one()
                    ops.pop()
                elif s[i] == '(': ops.append(s[i])      # is )
                elif s[i] in '+-*/':                    # is +-/*
                    if ops and ((s[i] in '+-' and ops[-1] in '+-') or ops[-1] in '*/'):
                        calc_one()
                    ops.append(s[i])
                # else is #, do nothing
        while ops: 
            calc_one()
        return nums[-1]

# test
so = Solution()
ans = so.calculate('1-1+1')
print(ans)
ans = so.calculate('1+4*(2-3)+(4/2+1)')
print(ans)
