#
# @lc app=leetcode id=2096 lang=python3
#
# [2096] Step-By-Step Directions From a Binary Tree Node to Another
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(ans, path, curr, target):
            if not curr:
                return False

            if curr.val == target:
                ans.append(path[:])
                return True 

            if curr.left:
                path.append((curr.left.val, 'L'))
                if dfs(ans, path, curr.left, target):
                    return True 
                path.pop() 
            
            if curr.right:
                path.append((curr.right.val, 'R'))
                if dfs(ans, path, curr.right, target):
                    return True 
                path.pop() 
            
            return False


        # 先把根结点到start和end的path分别记录下来
        # 两个路径分叉的起始点就是LCA，把LCA和左右两个分叉路径连接起来就是答案
        path_start, path_end = [], []
        dfs(path_start, [(root.val, '')], root, startValue)
        dfs(path_end, [(root.val, '')], root, destValue)
        #print(path_start)
        #print(path_end)
        path_start = path_start[0]
        path_end = path_end[0]

        i = 0
        while i < min(len(path_start), len(path_end)):
            if path_start[i] == path_end[i]:
                i += 1
            else:
                break 

        ans =[]
        for val, dir in path_start[i:][::-1]:
            ans.append('U')
        for val, dir in path_end[i:]:
            ans.append(dir)
        return ''.join(ans)



# @lc code=end

