""" Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

 

Example 1:

Input: [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
Example 2:

Input: [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output. """

from threading import Event
class Foo_Event: # event isSet() return the internal flag, set() to internal flag True, clear() to False, wait() block until the internal flag to true, the return is the internal flag.
    def __init__(self):
        self.e2 = Event()
        self.e3 = Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.e2.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
                
        self.e2.wait()
        printSecond()
        self.e3.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.e3.wait()
        printThird()


from threading import Lock
class Foo_Lock:
    def __init__(self):
        self.l2 = Lock()
        self.l2.acquire() # lock acquire will try to locks the lock and BLOCK until other thread release() it if locked, then it locks the lock again and return True.
        self.l3 = Lock()
        self.l3.acquire() 

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l2.release() # of course, one thread can release the lock which it doesn't acquire


    def second(self, printSecond: 'Callable[[], None]') -> None:
                
        self.l2.acquire()
        printSecond()
        self.l3.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.l3.acquire()
        printThird()