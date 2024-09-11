#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#

# @lc code=start
import random 

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        random.shuffle(points)
        self.sort(points, 0, len(points)-1, k)
        return points[:k]

    def sort(self, points, l, r, k):
        if l < r:
            p = self.partition(points, l, r)    
            if p == k:
                return 
            elif p < k:
                self.sort(points, p+1, r, k)
            else:
                self.sort(points, l, p-1, k)
    

    def partition(self, points, l, r):
        pivot = points[l]
        pivot_dist = self.distance(pivot)
        
        i = l 
        for j in range(l+1, r+1):
            if self.distance(points[j]) <= pivot_dist:
                i += 1
                points[j], points[i] = points[i], points[j]

        points[i], points[l] = points[l], points[i]
        return i

    def partitionR(self, points, l, r):
        pivot = points[r]
        pivot_dist = self.distance(pivot)
        i = l - 1
        for j in range(l, r):
            if self.distance(points[j]) <= pivot_dist:
                i += 1
                points[j], points[i] = points[i], points[j]
        points[i+1], points[r] = points[r], points[i+1]
        return i+1

    def distance(self, point):
        return point[0]**2 + point[1]**2
        
# @lc code=end

