#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 虚拟头节点
        dummy = curr = ListNode()

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1 
                list1 = list1.next 
            else:
                curr.next = list2
                list2 = list2.next 

            curr = curr.next 

        # 终止条件 list1 和 list2 有一个是空
        if list1:
            curr.next = list1 
        
        if list2:
            curr.next = list2 

        return dummy.next 
# @lc code=end

