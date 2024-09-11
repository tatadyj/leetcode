#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
from typing import List
import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            rest = first - second
            if rest != 0:
                heapq.heappush(stones, rest)

        if len(stones) == 0:
            return 0 
        else:
            return -heapq.heappop(stones)

Solution().lastStoneWeight([3,7,2])
        
# @lc code=end

