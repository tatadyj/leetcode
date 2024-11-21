#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#

# @lc code=start
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label >= 1:
            res.append(label)
            level = int(math.log2(label))
            label = label // 2
            # x - start = end - x*
            # x* = start + end - x
            start = 2**(level-1)
            end = 2**(level)-1
            label = start + end - label 
        return res[::-1]  
# @lc code=end

