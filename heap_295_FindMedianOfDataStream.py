'''
Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.
Examples:
[2,3,4] , the median is 3
[2,3] , the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the
data structure.
double findMedian() - Return the median of all elements so far.
'''
import heapq
class Solution():
    def __init__(self):
        self.maxHeap = [] # max number on the top of heap
        self.minHeap = [] # min number on the top of heap

    def addNum(self, num):
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.minHeap, num)
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
        else:
            heapq.heappush(self.maxHeap, -num)
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
         
    def findMedian(self):
        return -self.maxHeap[0] if len(self.maxHeap) == len(self.minHeap) + 1 else (-self.maxHeap[0] + self.minHeap[0])/2.0  # peek the heap in python is heap[0] 


# test
s = Solution()
for num in [2, 3, 4, -2, -3, -4]:
    s.addNum(num)
print(s.findMedian())