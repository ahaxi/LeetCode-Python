# Description #######################
# Reverse a singly linked list.
# ###################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        current = head  # Start of the beginning part
        prev = None
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node
        return prev        

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            
            slow = slow.next
            fast = fast.next.next
        return True
