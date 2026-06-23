class Solution(object):
    def isPalindrome(self, x):
        rev=0
        num=x
        while x>0:
            ld=x%10
            rev=rev*10+ld
            x=x//10
        if rev==num:
            return True
        else:
            return False
        