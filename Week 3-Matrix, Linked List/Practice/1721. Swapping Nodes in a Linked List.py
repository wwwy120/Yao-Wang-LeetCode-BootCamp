# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
    
        length = 0
        node = head
        while node:
            node = node.next
            length += 1
        
        node1 = node2 = head
        for i in range(k - 1):
            node1 = node1.next
        for i in range(length - k):
            node2 = node2.next
        
        node1.val, node2.val = node2.val, node1.val
        return head

