# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        #Step 1: find the middle node
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        
        half = length//2
        node = head
        for i in range(half):
            node = node.next
        
        #Step 2: reverse second half list
        middle = node
        curr = node
        prev = None
        nex = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr= nex
            try:
                nex = nex.next
            except:
                break
        middle = prev

        
        #Step 3: compare two parts
        node = head
        while middle:
            if node.val != middle.val:
                return False
            node = node.next
            middle = middle.next
        
        return True
        




        
