import threading
import concurrent.futures
import multiprocessing

def f():
    pass

t1 = threading.Thread(target=f)
t1.start()
t1.join()

with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(f)
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=f)
    p1.start()
    p1.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.submit(f)

""" thread and process share almost same methods, high level object like Lock, RLock, Event, Semaphore, Condition, Barrier, Timer 
Lock: 
has two states as unlocked and locked.  
acquire will blocked on locked until other thread release to unlocked, return immediately on unlocked and release.
Lock can't release on unlocked, will raise error, and one thread can release other thread's lock,
When release, only one of other thread will acquire the lock if multiple threads are acquiring. 

RLock, can recursively lock acquire on locked state when owned by thread itself, will increase recursive count by one. release will reduce count by one.
And thread can only release the lock owned by itself, can't release another thread's lock.

Event: like the lock, it has internal flag true and false. set() to true, clear() to false. Once set(), it will change all the wait() thread to free, not like lock only one thread.

Semaphore: has a internal atomic counter as the limits of the number of thread can pass at the same time in acquire(), 
which when acquire will reduce by one and when release will increase by one. It is very helpful to control a number of threads can do something first.

Condition: has a internal lock, but after acquire the internal lock, it can wait() for other threads to notify, when wait() it release the lock and wait for the notify.
The thread acquire the lock can notify others to wake up from wait() to acquire the lock. 

Barrier: it is a gate which how many threads need to acquire this barrier before them can pass. After passing, barrier will reset to zero.


"""

  
barrier = threading.Barrier(3) 
  
class thread(threading.Thread): 
    def __init__(self, thread_ID): 
        threading.Thread.__init__(self) 
        self.thread_ID = thread_ID 
    def run(self): 
        print(str(self.thread_ID) + "\n") 
        print("Parties = " + str(barrier.parties) + "\n")
        print("n_waiting = " + str(barrier.n_waiting) + "\n")  
        barrier.wait() 
        
        
          
thread1 = thread(100) 
thread2 = thread(101) 
  
thread1.start() 
thread2.start() 
  
thread5 = thread(104)
thread5.start()
  
#print(str(barrier.broken) + "\n") 
print("n_waiting after free = " + str(barrier.n_waiting))
print("parties after free = " + str(barrier.parties))
#barrier.reset() 
print("n_waiting after reset = " + str(barrier.n_waiting)) 
thread3 = thread(102)
thread3.start()
thread4 = thread(103)
thread4.start()
thread6 = thread(105)
thread6.start()



print("End") 
