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
        self.bottom = [] # the bottom heap (max heap) 
        self.top = [] # the top heap (min heap)

    def addNum(self, num):
        if len(self.bottom) == len(self.top):
            heapq.heappush(self.top, num)
            heapq.heappush(self.bottom, -heapq.heappop(self.top))
        else:
            heapq.heappush(self.bottom, -num)
            heapq.heappush(self.top, -heapq.heappop(self.bottom))
         
    def findMedian(self):
        
        return -self.bottom[0] if len(self.bottom) == len(self.top) + 1 else (-self.bottom[0] + self.top[0])/2.0  
    


# test
s = Solution()
for num in [2, 3, 4, -2, -3, -4]:
    s.addNum(num)
print(s.findMedian())