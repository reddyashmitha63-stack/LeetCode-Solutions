class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        size=len(nums)
        for i in range(size):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        result=[0]*size
        p=0
        n=1
        for i in range(len(pos)):
            result[p]=pos[i]
            p+=2
            result[n]=neg[i]
            n+=2
        return result