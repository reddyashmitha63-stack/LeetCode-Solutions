class Solution(object):
    def reverseWords(self, s):
        s1=s.split()
        n=len(s1)
        ans=[]
        for i in range(n-1,-1,-1):
            ans.append(s1[i])
        return ' '.join(ans)


        