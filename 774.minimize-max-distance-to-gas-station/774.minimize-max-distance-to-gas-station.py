#
# @lc app=leetcode id=774 lang=python3
#
# [774] Minimize Max Distance to Gas Station
#

# @lc code=start
def is_valid(val, distances, k):
    # max dist <= val, can we get by adding just less or equal than k new stations
    count = 0
    for dist in distances:
        count += (int(dist / val) + 1) - 1 # how many buckets - 1 = # of stations
    return count <= k


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        distances = []
        for i in range(1, len(stations)):
            distances.append(stations[i] - stations[i-1])
        
        left = 0
        right = max(distances)
        while right - left > 1e-6:
            mid = (left + right) / 2.0
            if is_valid(mid, distances, k):
                right = mid
            else:
                left = mid
        return right # left or right all ok
        
# @lc code=end

