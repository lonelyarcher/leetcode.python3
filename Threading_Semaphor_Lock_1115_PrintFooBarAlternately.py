""" Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will call bar(). Modify the given program to output "foobar" n times.

 

Example 1:

Input: n = 1
Output: "foobar"
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.
Example 2:

Input: n = 2
Output: "foobarfoobar"
Explanation: "foobar" is being output 2 times. """

from threading import Semaphore
# Semaphore will has usage quote in its state, so it easy to control when you need to limit executing times, like this question, foo one time, then bar one time, and so on
class FooBar:
    def __init__(self, n):
        self.n = n
        self.f = Semaphore(1)
        self.b = Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for _ in range(self.n):
            
            self.f.acquire()
            printFoo()
            self.b.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for _ in range(self.n):
            self.b.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.f.release()

from threading import Lock

class FooBar_Lock:
    def __init__(self, n):
        self.n = n
        self.l1, self.l2 = Lock(), Lock()
        self.l2.acquire() # initially lock the l2

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for _ in range(self.n):
            self.l1.acquire() # first will acquire immediately since l1 is not locked initially, then it locks it, so second loop will be blocked until thread bar to release l1. 
            printFoo()
            self.l2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for _ in range(self.n):
            self.l2.acquire() # will be blocked until thread foo finish print and release l2
            printBar()
            self.l1.release()