# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if head is None or head.next is None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        prev_group=dummy
        while True:
            kth=prev_group
            for i in range(k):
                kth=kth.next
                if kth is None:
                    return dummy.next
            group_next=kth.next
            prev=group_next
            current=prev_group.next
            while current!=group_next:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            temp = prev_group.next
            prev_group.next = prev
            temp.next = group_next
            prev_group = temp



        