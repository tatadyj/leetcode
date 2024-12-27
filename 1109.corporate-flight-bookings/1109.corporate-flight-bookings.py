#
# @lc app=leetcode id=1109 lang=python3
#
# [1109] Corporate Flight Bookings
#

# @lc code=start
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n+2)

        for first, last, seats in bookings:
            diff[first] += seats 
            diff[last+1] -= seats 

        res = []
        cumu_sum = 0 
        for i in range(1, len(diff)-1):
            cumu_sum += diff[i]
            res.append(cumu_sum)
        return res 
# @lc code=end

