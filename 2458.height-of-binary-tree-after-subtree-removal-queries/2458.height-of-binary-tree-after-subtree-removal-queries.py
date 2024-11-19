#
# @lc app=leetcode id=2458 lang=python3
#
# [2458] Height of Binary Tree After Subtree Removal Queries
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        depth_dict = defaultdict(list) # storing at a specific depth, what are those nodes. 
        depths = defaultdict(int) # storing depth of each node
        heights = defaultdict(int) # storing height of each node

        def dfs(curr, depth): # return height
            if not curr:
                return -1

            depth_dict[depth].append(curr.val)
            depths[curr.val] = depth
            left_height = dfs(curr.left, depth+1)
            right_height = dfs(curr.right, depth+1)
            heights[curr.val] += max(left_height, right_height) + 1
            return heights[curr.val] 

        dfs(root, 0)
        #print(depth_dict)
        #print(depths)
        #print(heights)

        for key in depth_dict:
            depth_dict[key] = [(heights[k], k) for k in depth_dict[key]]
            depth_dict[key].sort(reverse=True)

        ans = []
        for q in queries:
            depth = depths[q]
            max_height = depth - 1 # if the removed node has no brothers, select the depth of parent 
            for hi, nei in depth_dict[depth]:
                if nei != q: 
                    max_height = max(max_height, hi + depths[nei])
                    break 
            ans.append(max_height)
        return ans



# @lc code=end

