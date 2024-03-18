# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        if not head or not head.next:
            return head
        
        
        next_node = head.next
        new_head = head.next.next
        next_node.next = head

        head.next = self.swapPairs(new_head)

        return next_node

        
        
