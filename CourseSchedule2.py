import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        if not numCourses:
            return []

        pre = collections.defaultdict(set)
        nex = collections.defaultdict(set)
        for a, b in prerequisites:
            pre[a].add(b)
            nex[b].add(a)


        stack = [key for key in range(numCourses) if key not in pre]
        order = []
        while stack:
            cur = stack.pop()
            order.append(cur)
            if cur in nex:
                for child in nex[cur]:
                    pre[child].remove(cur)
                    if not pre[child]:
                        stack.append(child)
        return order if len(order)==numCourses else []

s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))