# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        slow=head
        fast=head
        prev=None
        while fast is not None and fast.next is not None:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=None
        mid=slow
        left=self.sortList(head)
        right=self.sortList(mid)
        return self.merge(left,right)
    def merge(self, first, second):
        if first is None:
            return second
        if second is None:
            return first
        if first.val<=second.val:
            finalHead=first
            first=first.next
        else:
            finalHead=second
            second=second.next
        finalTail=finalHead
        while first is not None and second is not None:
            if first.val<=second.val:
                finalTail.next=first
                finalTail=first
                first=first.next
            else:
                finalTail.next=second
                finalTail=second
                second=second.next
        if first is not None:
            finalTail.next=first
        else:
            finalTail.next=second
        return finalHead



        