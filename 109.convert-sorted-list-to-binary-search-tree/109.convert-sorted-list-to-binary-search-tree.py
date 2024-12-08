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
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return 
        
        if not head.next:
            root = TreeNode(head.val)
            return root

        if not head.next.next:
            root = TreeNode(head.val)
            root.right = TreeNode(head.next.val)
            return root

        fast, slow = head, head 
        prev = None
        while fast.next and fast.next.next:
            fast = fast.next.next 
            prev = slow
            slow = slow.next
        prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root
# @lc code=end

