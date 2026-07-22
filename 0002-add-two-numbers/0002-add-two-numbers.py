# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy=ListNode(0)
        current=dummy
        temp1=l1
        temp2=l2
        carry=0
        while temp1 or temp2 or carry:
            val1=temp1.val if temp1 else 0
            val2=temp2.val if temp2 else 0
            total=val1+val2+carry
            digit=total%10
            carry=total//10
            current.next = ListNode(digit)
            current = current.next
            if temp1:
                temp1=temp1.next
            if temp2:
                temp2=temp2.next
        return dummy.next

        