'''
给你一个string和x的value让你解出y的值
比如'2x - ((x - (3x + 1) + 2) + 3) + 4 = x + y'
'''

def caculate(s, xVal):
    l, r = s.split('=')
    al, bl, cl = processOneSide(l)
    ar, br, cr = processOneSide(r)
    return (cr - cl + (ar - al) * xVal) / (bl - br)

def processOneSide(s):
    a, b, c = 0, 0, 0
    tmp = 0
    cur_sign = 1
    stack = [1] # stack will hold the sign for this level ( current parenthesis block )
    for ch in s+' ': # extend the equation to handle the last numeric item
        if ch.isdigit():
            tmp = tmp * 10 + int(ch)
        else:
            if ch == 'x':
                a += cur_sign * (tmp if tmp else 1)
            elif ch == 'y':
                b += cur_sign * (tmp if tmp else 1)
            else:
                c += tmp # c accumulate if not nx or ny
                if ch == '(':  # push the cur sign to the stack
                    stack.append(cur_sign)
                elif ch == ')': # return to previous level of stack for last cur_sign
                    stack.pop()
                elif ch == '-':
                    cur_sign = -1 * stack[-1] 
                elif ch == '+':
                    cur_sign = stack[-1]
            tmp = 0 # if not digit, reset tmp to 0
    return (a, b, c)
            
# Test
s = '2x - (4x+ y) = 1'
print(caculate(s, 1))
s = '2x - ((x - (3x + 1) + 2) + 3) + 4 = x + y'
1 - 2 - 3 + 4
print(caculate(s, 1))