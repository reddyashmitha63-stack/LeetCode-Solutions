class Solution(object):
    def processStr(self, s):
        s=list(s)
        size=len(s)
        result=[]
        for i in range(size):
            if s[i]=='#':
                result=result+result
            elif s[i]=='%':
                result.reverse()
            elif s[i]=='*':
                if result:
                    result.pop()
            else:
                result.append(s[i])
        return "".join(result)