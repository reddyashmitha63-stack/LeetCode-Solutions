class Solution(object):
    def largestOddNumber(self, num):
        max = ""

        for i in range(len(num)-1, -1, -1):
            if int(num[i]) % 2 == 1:
                if len(num[:i+1]) > len(max):
                    max = num[:i+1]

        return max