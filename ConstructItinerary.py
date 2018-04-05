import collections
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets List[List[str]]
        :rtype List[str]
        """
        flights = collections.defaultdict(list)
        for c1, c2 in tickets:
            flights[c1].append(c2)
        for k in flights:
            flights[k].sort()
        itin = ["JFK"]
        self.recursion("JFK", itin, flights, len(tickets) + 1)
        return itin
    def recursion(self, cur, itin, flights, n):  
        if len(itin) == n:
            return True
        for i in range(len(flights[cur])):
            nex = flights[cur].pop(i)
            itin.append(nex)
            if self.recursion(nex, itin, flights, n):
                return True           
            flights[cur].insert(i, nex)
            itin.pop()
        return False
s = Solution()
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
s = Solution()
print(s.findItinerary(tickets))



