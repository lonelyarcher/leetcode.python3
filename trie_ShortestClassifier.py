'''
给出几个二进制数…如何找到最小的连续bit位数以区别这几个二进制数？比如我
1000 0100 0010这三个数…我只要前两位就能区别了。
'''
from math import inf
class Solution():
    def minPrefixLength(self, nums):
        """
        :type nums: List[str]
        :rtype: int
        """
        root = {}
        if not nums or len(nums) == 1: return 0
        maxDepth, minDepth = -inf, inf
        for i in range(len(nums)):
            cur = root
            depth = 1
            found = False
            for c in nums[i]:
                if c not in cur and i != 0 and not found:
                    maxDepth = max(maxDepth, depth)
                    minDepth = min(minDepth, depth)
                    found = True
                cur = cur.setdefault(c, {})
                depth += 1
        
        print(maxDepth, minDepth)       
        return maxDepth - minDepth + 1

#test cases:
so = Solution()
print(so.minPrefixLength(['1000', '0100', '0010']))
print(so.minPrefixLength(['11110100', '11111000', '11111100']))