#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1 

        tank, start = 0, 0  
        # 已经确保有解的情况下， 解必须在0，n-1中
        # 如果从0到n-2都不能立，n-1必然为解
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0 
                start = i + 1 
        return start 

# @lc code=end

