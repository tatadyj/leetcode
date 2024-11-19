#
# @lc app=leetcode id=1522 lang=python3
#
# [1522] Diameter of N-Ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        max_diameter = 0 

        def dfs(curr):
            nonlocal max_diameter

            if not curr.children:
                return 1

            child_list = sorted([dfs(child) for child in curr.children], reverse=True)
            if len(child_list) > 1:
                max_diameter = max(max_diameter, child_list[0] + child_list[1])
            else:
                max_diameter = max(max_diameter, child_list[0])
            return max(child_list) + 1

        dfs(root)
        return max_diameter

# @lc code=end

