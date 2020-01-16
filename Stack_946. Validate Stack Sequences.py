""" Given two sequences pushed and popped with distinct values, return true if and only if this could have been the result of a sequence of push and pop operations on an initially empty stack.

 

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.
 

Note:

0 <= pushed.length == popped.length <= 1000
0 <= pushed[i], popped[i] < 1000
pushed is a permutation of popped.
pushed and popped have distinct values. """
from typing import List
class Solution:
    # from popped list, if saw a large idx, so the idx before it should all be pushed.
    # else then should be popped, it not same as top of stack return false
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx = {v: i for i, v in enumerate(pushed)} # idx map from element to its index in pushed array
        pushed = [i for i in range(len(pushed))]
        st, end = [], -1
        for i in popped:
            if not st or idx[i] > end:
                st.extend(pushed[end + 1:idx[i]])
                end = idx[i]
            elif idx[i] != st.pop():
                return False
        return True

    '''
    Better solution, go from pushed list, simulate the process, first push into the first element of pushed array.
    then you have two choice, keep pushed the left elements or popout it.
    so we can compare st[-1] with beginning of popped array, if same, which means we pop first, else we keep pushing next pushed elements
    '''
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for i in pushed:
            st.append(i)
            while st and st[-1] == popped[j]:
                st.pop()
                j += 1
        return not st

print(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,5,3,2,1])) #true
print(Solution().validateStackSequences(pushed = [1,2,3,4,5], popped = [4,3,5,1,2])) #false