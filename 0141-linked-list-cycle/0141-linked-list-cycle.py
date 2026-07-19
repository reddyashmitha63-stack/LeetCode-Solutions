# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        temp=head
        nodemap={}
        while temp is not None:
            if temp in nodemap:
                return True
            nodemap[temp]=1
            temp=temp.next
        return False

      
        