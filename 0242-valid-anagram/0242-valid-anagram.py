class Solution(object):
    def isAnagram(self, s, t):
        n=len(s)
        m=len(t)
        if n!=m:
            return False
        return sorted(s)==sorted(t)
        
        