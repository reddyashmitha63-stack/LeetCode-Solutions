class Solution(object):
    def majorityElement(self, nums):
        freq = {}
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        ans = []
        n = len(nums) // 3
        
        for key, value in freq.items():
            if value > n:
                ans.append(key)
        
        return ans