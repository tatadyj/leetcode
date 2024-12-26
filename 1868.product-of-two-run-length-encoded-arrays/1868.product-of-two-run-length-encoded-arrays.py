#
# @lc app=leetcode id=1868 lang=python3
#
# [1868] Product of Two Run-Length Encoded Arrays
#

# @lc code=start
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0 

        while i < len(encoded1) and j < len(encoded2):
            v1, f1 = encoded1[i]
            v2, f2 = encoded2[j]

            new_v, new_f = v1*v2, min(f1, f2)

            encoded1[i][1] -= new_f
            encoded2[j][1] -= new_f 

            if encoded1[i][1] == 0:
                i += 1 
            
            if encoded2[j][1] == 0:
                j += 1

            if not res or res[-1][0] != new_v:
                res.append([new_v, new_f])
            else:
                res[-1][1] += new_f 

        return res
# @lc code=end

