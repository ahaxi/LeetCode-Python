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
