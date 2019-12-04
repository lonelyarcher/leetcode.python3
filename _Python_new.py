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
A = {0, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
print(A | B == {0, 1, 2, 3, 4, 5, 6, 8}) #True
print(A & B == {2, 4}) #True
print(A - B == {0, 6, 8}) #True
print(A ^ B == {0, 1, 3, 5, 6, 8}) #True
# Python operations on Counter, 
# + addition of count
# - substraction, keep only positive counts
""" t1 : Counter({'e': 4, 'b': 4, 'a': 3, 'c': 2, 'd': 1})
t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'e': 2, 'b': 2})
t1&t2 : Counter({'c': 2, 'a': 2, 'e': 2, 'b': 2, 'd': 1}) """
# | Union, keep the maximum counts
""" t1 : Counter({'b': 4, 'e': 4, 'a': 3, 'c': 2, 'd': 1})
t2 : Counter({'c': 4, 'd': 3, 'a': 2, 'b': 2, 'e': 2})
t1|t2 : Counter({'b': 4, 'e': 4, 'c': 4, 'a': 3, 'd': 3}) """ 
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

print(" ".join([str(i) for i in range(10)]))



