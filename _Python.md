1. yield for, generator to sub-function including recursion, send(val), val will replace yield expression and continue
2. generator will raise StopIteration, next(gen, None) will return None when end
3. coroutines (the function you can run and pause, like generator) vs subroutine
4. event loop (programming construct which waits for or dispatches events or messages) implemented by 'asyncio', async def function / await coroutine/awaitable
5. sum with start=, min, max with default=, itertools.accumulate initial=
6. tuple comparison: (2, 9) < (3, 0)
7. when loop two iterables at the same time, use zip(l1, l2) 
8. use dictionary comprehension {key: val for k in list if k}
9. operator.add sub mul and_ or_ concat
10. list comprehension with double loops, always first loop is big one, like rows, outer list, then columns, list element.  m[row][col] for row in matrix for col in row, row can't appear after "in" first, but for 2 dimension list is on the contrary
11. bin str -> int int(n, 2), int -> bin str bin(num) = '0b1100111'
12. operator precedence: **, ~+-, */%//, +-, <<>> ,&^| ,in not in is not is ,< > <= >= != ==, = += -= *= /=, not and or
bit operator <<>>, &^| after */+-, then in not in, comparison <>==, then assignment, then and or
prone to errors:
    1. forget self
    2. mess with array idx and value,  == and =, for if forget end with :
    3. while loop move the idx, forget set restriction on idx < len(arr)
    4. when need to judge >= < or which side? slow down and draw a picture. like binary search, which side to abandon
    5. multiple corner cases, slow down to list all possibilities. maintain multiple flags and status variables is workable, but don't forget to update/maintain, write down a list on whiteboard, check on every conditions



BIT: construct [0] * (n + 1), update while <= n, i += lowbit, query while > 0, i -= lowbit i&-i
Segment Tree: Node: start, end, val, left, right, from arr, construct recursive from root, update, query by range, good for range update

