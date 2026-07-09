class Solution(object):
    def frequencySort(self, s):
        s = sorted(s)

        arr = []
        i = 0

        while i < len(s):
            count = 1
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            arr.append((count, s[i]))
            i += 1

        arr.sort(reverse=True)

        ans = ""
        for count, ch in arr:
            ans += ch * count

        return ans