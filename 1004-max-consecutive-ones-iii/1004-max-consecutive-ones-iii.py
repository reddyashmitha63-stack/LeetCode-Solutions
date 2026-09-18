class Solution(object):
    def longestOnes(self, nums, k):
        n = len(nums)
        start = 0
        count = 0
        max_len = 0

        for i in range(n):
            if nums[i] == 0:
                count += 1

            while count > k:
                if nums[start] == 0:
                    count -= 1
                start += 1

            max_len = max(max_len, i - start + 1)

        return max_len