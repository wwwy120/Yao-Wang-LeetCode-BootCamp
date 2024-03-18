# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        #Time Complexity: O(n)
        #Space Complexity: O(1)
        if not head:
            return
        
        start = end = head
        for i in range(k):
            if not end:
                return head
            end = end.next
        
        new_head = self.reverse(start, end)
        start.next = self.reverseKGroup(end, k)

        return new_head    

    def reverse(self, start, end):
        prev = None
        while start != end:
            start.next, start, prev = prev, start.next, start
        return prev
