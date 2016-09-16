# Description #######################
# Reverse a singly linked list.
# https://leetcode.com/problems/linked-list-cycle-ii/
# ###################################

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        usedNode = set()
        while head is not None:
            if head in usedNode:
                return head
            else:
                usedNode.add(head)
                head = head.next
        return None
        
# Solution 2
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        
        return None
