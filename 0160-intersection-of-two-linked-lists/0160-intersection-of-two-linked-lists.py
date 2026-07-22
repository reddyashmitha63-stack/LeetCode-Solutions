# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        def length(head):
            count = 0
            temp = head
            while temp:
                count += 1
                temp = temp.next
            return count
        m=length(headA)
        n=length(headB)
        diff=abs(m-n)
        if m>n:
            long=headA
            short=headB
        else:
            long=headB
            short=headA
        while diff>0:
            long=long.next
            diff-=1
        while long is not None and short is not None:
            if long==short:
                return long
            long=long.next
            short=short.next
        return None
        