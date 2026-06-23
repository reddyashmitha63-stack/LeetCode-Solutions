class Solution(object):
    def nextPermutation(self, nums):

        n = len(nums)

        ind = -1

      
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                ind = i
                break

        # last permutation
        if ind == -1:
            nums.reverse()
            return

        # find next greater element
        for i in range(n-1, ind, -1):
            if nums[i] > nums[ind]:
                nums[i], nums[ind] = nums[ind], nums[i]
                break

        # reverse suffix
        left = ind + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1