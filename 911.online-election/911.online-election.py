#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#

# @lc code=start
import bisect 
from collections import defaultdict
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leads = []
        self.times = times 
        lead = persons[0]
        freq = defaultdict(int)
        for t,p in zip(times, persons):
            freq[p]+= 1
            if freq[p] >= freq[lead]:
                lead = p
            self.leads.append(lead)

    def q(self, t: int) -> int:
        idx = bisect.bisect_right(self.times, t)
        return self.leads[idx-1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

