""" In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0]. """

from typing import List
import collections
import bisect
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.winners = [] #pre calculate the winner at each time point
        self.times = times
        cnt = collections.defaultdict(int) # count on votes on each person. Since it it accumulating and updating on each steps, Counter is not helpful
        leading = persons[0]
        for i in range(len(times)):
            cnt[persons[i]] += 1
            if persons[i] != leading and cnt[persons[i]] >= cnt[leading]: # maintain the max votes count person
                leading = persons[i]
            self.winners.append(leading)

    def q(self, t: int) -> int:
        return self.winners[bisect.bisect_right(self.times, t) - 1] # find the last times index less than or equals to target t
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)