""" You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the list.
You need to use the following functions to access the linked list (you can't access the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
The input is only given to initialize the linked list internally. You must solve this problem without modifying the linked list. In other words, you must operate the linked list using only the mentioned APIs.

 

Follow up:

Could you solve this problem in:

Constant space complexity?
Linear time complexity and less than linear space complexity?
 

Example 1:

Input: head = [1,2,3,4]
Output: [4,3,2,1]
Example 2:

Input: head = [0,-4,-1,3,-5]
Output: [-5,3,-1,-4,0]
Example 3:

Input: head = [-2,0,6,4,4,-6]
Output: [-6,4,4,6,0,-2]
 

Constraints:

The length of the linked list is between [1, 1000].
The value of each node in the linked list is between [-1000, 1000] """

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:

    #Time O(n) Space O(n)
    def printLinkedListInReverse_Recursion(self, head: 'ImmutableListNode') -> None:
        if head:
            self.printLinkedListInReverse(head.getNext())
            head.printValue()

    #Time O(n^2) Space O(1)
    def printLinkedListInReverse_1(self, head: 'ImmutableListNode') -> None:
        n, p = 0, head
        while p:
            n += 1
            p = p.getNext()
        for i in range(n, 0, -1):
            p = head
            for j in range(i - 1):
                p = p.getNext()
            p.printValue()

    #Time O(n) O(sqrt(n))
    #divide the list to sqrt(n) chunk, then reverse each chunk, and print the chunks reversely
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        n, p = 0, head
        while p: #find out total size n
            n += 1
            p = p.getNext()
        m = int(n ** 0.5) + 1
        i, p, list = 0, head, [] #save each sqrt chunk's beginning node into the list
        while p:
            if i % m == 0:
                list.append(p)
            p = p.getNext()
            i += 1
        for i in range(len(list) - 1, -1, -1): # iterate chunks reversely
            p = list[i]
            res = []
            while p and (i == len(list) - 1 or p != list[i + 1]): # save this chunk into a temp list
                res.append(p)
                p = p.getNext()
            for q in res[::-1]: q.printValue() #print this chunk's reverse order 