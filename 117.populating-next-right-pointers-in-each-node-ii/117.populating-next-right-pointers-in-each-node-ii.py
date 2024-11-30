#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        queue = deque([root])
        while queue:
            size = len(queue)
            prev = None
            for _ in range(size):
                curr = queue.popleft()
                if prev:
                    prev.next = curr
                prev = curr 
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        return root

        # @lc code=end

