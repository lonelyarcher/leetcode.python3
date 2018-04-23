class Solution():
    def add(self, num1, num2):
        '''
        type: num1, num2: str
        rtype: str
        '''
        # align the decimal point
        p1, p2 = num1.find('.'), num2.find('.')
        if p1 > p2:
            num1, num2, p1, p2 = num2, num1, p2, p1
        num1 = '0'*(p2 - p1) + num1
        
        # loop the small length number 
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        carry = 0
        s1, s2 = list(num1), list(num2) # string is immutable, so convert it to list
        for i in range(len(s1) - 1, -1, -1):
            if s1[i] != '.':
                s = int(s1[i]) + int(s2[i]) + carry
                s2[i] = str(s % 10)
                carry = s // 10
        if carry > 0:
            s2 = ['1'] + s2
        return "".join(s2)
        
# test
print(Solution().add("123.456","999876.6"))