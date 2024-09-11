#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
#

# @lc code=start
from typing import List 

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
       
        q = [[findFirstOne(m)+1, i] for i,m in enumerate(mat)]

        q.sort()

        #res = heapq.nsmallest(k, q, key=lambda x:x[1])


        return [q[i][1] for i in range(k)]

    def findFirstOne(self, row):
                l, r = 0, len(row)-1
                while l < r:
                    mid = (l + r) // 2
                    if row[mid] == 0:
                        r = mid - 1
                    else:
                        l = mid 
                return l 

print(Solution().findFirstOne([1,1,1,1]))
# @lc code=end

