#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 

        slow = fast = head 

        while fast:
            if fast.val != slow.val:
                slow.next = fast 
                slow = slow.next 
            
            fast = fast.next


        return head 
# @lc code=end

