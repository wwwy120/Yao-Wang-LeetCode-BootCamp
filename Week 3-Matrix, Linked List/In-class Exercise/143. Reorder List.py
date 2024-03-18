# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        #Step 1: Find the middle node
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length <= 2:
            return head
        middle_length = length //2
        
        middle = head
        for i in range(middle_length):
            middle = middle.next
        middle_next = middle.next
        middle.next = None
        middle = middle_next
        

        #Step 2: Reverse the second half of the list
        prev = None
        curr = middle
        nex = curr.next
        while curr:
            curr.next = prev
            prev = curr
            curr = nex
            try: 
                nex = nex.next
            except:
                break
        middle = prev

        #Step 3: Reorder the list
        curr1 = head
        curr2 = middle
        next1 =head.next
        next2 = middle.next
        while curr2:
            curr1.next = curr2
            curr2.next = next1
            curr1 = next1
            curr2 = next2
            try:
                next1 = next1.next
                next2 = next2.next
            except:
                break
        return head
        
        return head
        
