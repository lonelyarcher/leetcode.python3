1. yield for, generator to sub-function including recursion, send(val), val will replace yield expression and continue
2. generator will raise StopIteration, next(gen, None) will return None when end
3. coroutines (the function you can run and pause, like generator) vs subroutine
4. event loop (programming construct which waits for or dispatches events or messages) implemented by 'asyncio', async def function / await coroutine/awaitable
5. sum with start=, min, max with default=, itertools.accumulate initial=
6. tuple comparison: (2, 9) < (3, 0)
7. when loop two iterables at the same time, use zip(l1, l2) 

prone to errors:

1. forget self
2. mess with array idx and value.
3. while loop move the idx, forget set restriction on idx < len(arr)
