#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def binarySearch(nums):
    if not nums:
        return 

    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = binarySearch(nums[:mid])
    root.right = binarySearch(nums[mid+1:])

    return root 

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return binarySearch(nums)
# @lc code=end

