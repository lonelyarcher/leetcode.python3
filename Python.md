1. yield for, generator to sub-function including recursion, send(val), val will replace yield expression and continue
2. generator will raise StopIteration, next(gen, None) will return None when end
3. coroutines (the function you can run and pause, like generator) vs subroutine
4. event loop (programming construct which waits for or dispatches events or messages) implemented by 'asyncio', async def function / await coroutine/awaitable
