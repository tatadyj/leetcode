#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#

# @lc code=start
from collections import defaultdict
from typing import List

def bt()

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dict = defaultdict(list)
        for item in tickets:
            dict[item[0]].append(item[1])
        
# @lc code=end

