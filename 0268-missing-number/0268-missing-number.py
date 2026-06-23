class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expected_sum=(n*(n+1))//2
        actual_sum=0
        for i in range(n):
            actual_sum+=nums[i]
        missing_number=expected_sum-actual_sum
        return missing_number
        