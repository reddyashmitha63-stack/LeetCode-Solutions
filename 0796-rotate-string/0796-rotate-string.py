class Solution(object):
    def rotateString(self, s, goal):
        n=len(s)
        m=len(goal)
        if n!=m:
            return False
        s1=s+s
        if goal in s1:
            return True
        else:
            return False

        