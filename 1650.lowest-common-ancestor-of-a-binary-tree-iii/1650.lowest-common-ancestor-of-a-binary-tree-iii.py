#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 记录 p，q 到跟节点的路径 
        # 根据它们路径，反转找到最后一个共同节点
        p_path, q_path = [], []

        while p:
            p_path.append(p)
            p = p.parent 

        while q:
            q_path.append(q)
            q = q.parent 

        p_path = p_path[::-1]
        q_path = q_path[::-1]
        i = 0 
        while i < len(p_path) and i < len(q_path) and p_path[i] == q_path[i]:
            i += 1 
        
        return p_path[i-1]

        
        
# @lc code=end

