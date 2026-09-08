class Solution(object):
    def countCommas(self, n):
        if n < 1000:
            count = 0
        elif n < 1000000:
            count = n - 999
        else:
            count = 999000 + (n - 999999) * 2
        return count