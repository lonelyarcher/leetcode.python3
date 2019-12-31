# generate comprehesion omit parenthesis
print(sum(i for i in range(10))) #45
# maximum / minimum number in python:
print(float('inf'), float('-inf')) #inf -inf
# unpack in python
print(*[1, 2, 3]) # 1,2,3
dict = { 'hello': 1, 'bye': 2 };
def p(bye, hello):
    print(bye, hello)
p(**dict) # 2, 1


# Python local variable no need to define first, hoist to top of function
# Python false values: empty sequence [] '' (), empty mapping {},  0 and None, 0 is false need be careful in algorithm condition
# python == compare by value, is by object address, int and small str are singleton, so same address like java
print("abcd" is "abcd") #True

#Python dict: d.values(), d.items(), d.keys(), sorted(d) = sorted(d.keys()) 

# Python operations on set
# union:| intersections: & difference from first to the seconde: -, ^ symmetric difference
# set add() update() remove(), list append() extend() pop() remove() different(*othersets) union(*othersets) intersection(*othersets) different_symmetric(other)
# dictionary update(other dict or key/value pairs)
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print(A | B == {0, 1, 2, 3, 4, 5, 6, 8}) #True
print(A & B == {2, 4}) #True
print(A - B == {0, 6, 8}) #True
print(A ^ B == {0, 1, 3, 5, 6, 8}) #True Return a new set with elements in either the set or other but not both.
# Python operations on Counter, 
# + addition of count
# - substraction, keep only positive counts
""" t1 : Counter({'e': 4, 'b': 4, 'a': 3, 'c': 2, 'd': 1})
t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'e': 2, 'b': 2})
t1 & t2 : Counter({'c': 2, 'a': 2, 'e': 2, 'b': 2, 'd': 1}) """
# | Union, keep the maximum counts
""" t1 : Counter({'b': 4, 'e': 4, 'a': 3, 'c': 2, 'd': 1})
t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'b': 2, 'e': 2})
t1 | t2 : Counter({'b': 4, 'e': 4, 'c': 4, 'a': 3, 'd': 3}) """ 
# Intersections: &, keep only the min counts
""" t1 : Counter({'e': 4, 'b': 4, 'a': 3, 'c': 2, 'd': 1})
t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'e': 2, 'b': 2})
t1&t2 : Counter({'c': 2, 'a': 2, 'e': 2, 'b': 2, 'd': 1}) """

#bisect.bisect() = bisect.bisect_right() find first GT, bisect.bisect_left() find first GE

#heapq, if heap need key or cmp, pass the key into the tuple with element and push tuple into the heap
import heapq
heap = [1, 2, 3]
heapq.heapify(heap)
heapq.heappush(heap, 0) 
heapq.heappop(heap)
heapq.heappushpop(heap, 5)

# Python string and number are not auto-boxing, make sure to convert to correct type
print(" ".join([str(i) for i in range(10)]))

# expression assignment, 
# 1. while loop while x := read(file): print(x)
# 2. boolean complex expression, 
if (x:=1) == 1 and x > 0: print(x) 
# 3. list [x:=1, x + 1] = [1, 2]

class AA(object):
    def __getitem__(self, arg):
        return arg
obj = AA()
obj.a = 1
print(obj['a'])
print(obj.a)

""" Python mistakes: 
1. Methods forget self. 
2. variable name coincide with existing/system function name. 
3. generator and iterator can only iterate once
 """

import collections
queue = collections.deque
if queue:
    print('empty queue is true')
else:
    print('empty deque is false')

arr = [0] * 2 # python [] will raise outOfIndex error when access unassigned list index
arr[1] = "a"
print(arr)

str1 = sorted("abcd")
str1[:] = str1[::-1] #slice assignment, it alter the array in place.  not like the slicing which return a copy a = b[:]
print(str1)

#list.reverse() return None, if you want to return reversed copy use list[::-1]

x = y = z = 3
print(x, y, z)

# assignment expr can not assign to tuple in left
# comparison tuple
print([4, 2] > [3, 9])
print(tuple([4, 2]) > (3, 9))
print((4, 2) > (3, 9))


#f string
x, y = 3, 3.1415926 
print(f"x={x} y={y:.2f}")
print(sorted('ababcaa'))


#flat list of list
l = [[1, 2], [3]]
print([item for sublist in l for item in sublist]) 
print(sum(l, [])) # print(sum(l, start=[])) both are OK, because no * in sum method argument signature
import operator, functools, itertools
print(functools.reduce(operator.add, l)) # operator.concat is also OK here
print(list(itertools.chain(*l)))
print([1, 2] == [1, 2])
print(float("inf") - float("inf"))
print("-".join("abc"))
print(len(list(itertools.combinations(range(10), 2))))