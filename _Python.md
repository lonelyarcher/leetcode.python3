1. yield for, generator to sub-function including recursion, send(val), val will replace yield expression and continue
2. generator will raise StopIteration, next(gen, None) will return None when end
3. coroutines (the function you can run and pause, like generator) vs subroutine
4. event loop (programming construct which waits for or dispatches events or messages) implemented by 'asyncio', async def function / await coroutine/awaitable
5. sum with start=, min, max with default=, itertools.accumulate initial=
6. tuple comparison: (2, 9) < (3, 0)
7. use dictionary comprehension {key: val for k in list if k}
8. operator.add sub mul and_ or_ concat
9. list comprehension with double loops, always first loop is big one, like rows, outer list, then columns, list element.  m[row][col] for row in matrix for col in row, row can't appear after "in" first
10. check error: mess up list index and elements, == and =, for if forget end with :
11. bin str -> int int(n, 2), int -> bin str bin(num) = '0b1100111'