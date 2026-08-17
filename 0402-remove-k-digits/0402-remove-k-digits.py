class Solution(object):
    def removeKdigits(self, num, k):
        st=[]
        for digit in num:
            while st and k>0 and st[-1]>digit:
                st.pop()
                k-=1
            st.append(digit)
        if k>0:
            st=st[:-k]
        if not st:
            return "0"
        result=''.join(st).lstrip('0')
        if result=="":
            return "0"
        return result
        