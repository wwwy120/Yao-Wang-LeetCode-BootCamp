# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        middle = fast = head
        while fast != None and fast.next != None:
            middle = middle.next
            fast = fast.next.next
        return middle
        
