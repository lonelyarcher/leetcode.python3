'''
找sum最大，每个长度都是k 的三个subarray。 三个subarray不能有overlap。 举个
栗子
nums = [1,2,1,2,6,7,5,1]
k = 2
这个里面找到的就应该是
[1,2],[2,6],[7,5]
'''
from math import inf
class Solution(object):
    def largestSubSum(self, nums, k):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) # dp better use 0 to n inclusively, will one more element that the object list
        # max sum of one k length subarray
        s1 = [-inf for _ in range(k)] 
        for i in range(k, n + 1):  # can't use list comprehension, because the comprehension can't refer itself like s1[i] need to refer s1[-1]
            s1.append(max(sum(nums[i - k: i]), s1[-1])) 
        # max sum of two k length subarray
        s2 = [-inf for _ in range(2*k)]
        for i in range(2*k, n + 1):
            s2.append(max(sum(nums[i - k: i]) + s1[i - k], s2[-1]))
        # max sum of three k length
        s3 = [-inf for _ in range(3*k)]
        for i in range(3*k, n + 1):
            s3.append(max(sum(nums[i - k: i]) + s2[i - k], s3[-1])) 
        return s3[n]
print(Solution().largestSubSum([1,2,1,2,6,7,5,1], 2))