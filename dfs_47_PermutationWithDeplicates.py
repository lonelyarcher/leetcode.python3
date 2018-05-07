class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        visited = [False] * n
        res = []

        def dfs(cur):
            if len(cur) == n:
                res.append(cur[:])
            for i in range(n):
                if not visited[i] and not ( i > 0 and nums[i] == nums[i - 1] and not visited[i - 1] ):
                    cur.append(nums[i])
                    visited[i] = True
                    dfs(cur)
                    cur.pop()
                    visited[i] = False 

        dfs([])
        return res

# test
print(Solution().permuteUnique([1,2,0,0]))