def lcm(x, y):
    return x * y / gcd(x, y)

def gcd(x, y):
    r = x % y
    return gcd(y, r) if r else y

import functools
def lcmAll(sequence):
    return functools.reduce(lcm, sequence)


print(gcd(8, 6))
print(lcm(6, 8))
print(lcmAll([4,6,8,12]))