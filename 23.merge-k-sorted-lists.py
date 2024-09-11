#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        dummy = curr = ListNode()
        # heapq 处理重复值
        q = []
        

        for i,l in enumerate(lists):
            if l:
                heapq.heappush(q, (l.val, i, l))

        while q:
            _, idx, node = heapq.heappop(q)
            curr.next = node 
            curr = curr.next 
            node = node.next 
            if node:
                heapq.heappush(q, (node.val, idx, node))

        return dummy.next 

# @lc code=end

