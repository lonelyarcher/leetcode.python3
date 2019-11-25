# generate comprehesion omit parenthesis
print(sum(i for i in range(10)))
# maximum / minimum number in python:
print(float('inf'), float('-inf'))
# unpack in python
print(*[1, 2, 3])
dict = { 'hello': 1, 'bye': 2 };
def p(bye, hello):
    print(bye, hello)
p(**dict)


# Python local variable no need to define first, hoist to top of function
# Python false values: empty sequence [] '' (), empty mapping {},  0 and None, 0 is false need be careful in algorithm condition
# python == compare by value, is by object address, int and small str are singleton, so same address like java
print("abcd" is "abcd")
