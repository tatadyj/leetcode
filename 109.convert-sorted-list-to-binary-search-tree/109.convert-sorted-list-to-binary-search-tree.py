#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def binarySearch(curr):
    if not curr:
        return

    if not curr.next:
        return TreeNode(curr.val)

    fast, slow, prev = curr, curr, None
    while fast and fast.next:
        prev = slow
        slow = slow.next 
        fast = fast.next.next
    prev.next = None
    root = TreeNode(slow.val)

    root.left = binarySearch(curr)
    root.right = binarySearch(slow.next)

    return root

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        return binarySearch(head)
# @lc code=end

