# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None or head.next is None:
            return None
        prev=ListNode(0)
        prev.next=head
        slow=prev
        fast=prev
        for i in range(n+1):
            fast=fast.next
        while fast is not None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return prev.next
        
        