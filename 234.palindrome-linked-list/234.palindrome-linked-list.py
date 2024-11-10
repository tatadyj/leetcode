#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. slow, fast pointers 
        slow = fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # 2. slow points to mid or mid-left element
        # 3. reverse linkedlist with slow.next as head
        curr = slow.next
        slow.next = None
        prev = None

        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 4. compare two linkedlist
        while prev != None and head != None:
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next 

        return True
        
        
# @lc code=end

