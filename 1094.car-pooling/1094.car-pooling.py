#
# @lc app=leetcode id=1094 lang=python3
#
# [1094] Car Pooling
#

# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1002

        for numPassengers, from_i, to_i in trips:
            if numPassengers > capacity:
                return False 
            diff[from_i] += numPassengers
            diff[to_i] -= numPassengers 


        cumu_sum = 0 
        for i in range(1, len(diff)-1):
            cumu_sum += diff[i]
            if cumu_sum > capacity:
                return False 
        return True       
# @lc code=end

