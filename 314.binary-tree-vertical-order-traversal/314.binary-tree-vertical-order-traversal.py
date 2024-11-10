#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def verticalOrder_bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    queue = deque([(root, 0)])
    pos_dict = defaultdict(list)
    while queue:
        size = len(queue)
        for _ in range(size):
            curr, pos = queue.popleft()
            pos_dict[pos].append(curr.val)
            if curr.left: queue.append((curr.left, pos-1))
            if curr.right: queue.append((curr.right, pos+1))

    return [val for _, val in sorted(pos_dict.items())]

from collections import deque, defaultdict

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pos_dict = defaultdict(list)
        def dfs(curr, depth, offset):
            if not curr: return 
            pos_dict[offset].append((depth, curr.val)) 
            dfs(curr.left, depth+1, offset-1)
            dfs(curr.right, depth+1, offset+1)

        dfs(root, 0, 0)
        #print(pos_dict)
        return [[v for d,v in sorted(val, key=lambda x: x[0])] for key, val in sorted(pos_dict.items())]
        
# @lc code=end

