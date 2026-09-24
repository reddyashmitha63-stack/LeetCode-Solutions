class Solution(object):
    def characterReplacement(self, s, k):
        n=len(s)
        left=0
        count={}
        max_len=0
        for right in range(n):
            count[s[right]]=count.get(s[right], 0) + 1
            max_freq=max(count.values())
            while (right-left+1)-max_freq>k:
                count[s[left]]-=1
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len
        
        