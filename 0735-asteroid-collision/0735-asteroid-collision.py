class Solution(object):
    def asteroidCollision(self, asteroids):
        n=len(asteroids)
        st=[]
        for i in range(n):
            current=asteroids[i]
            while st and st[-1]>0 and current<0:
                if abs(st[-1])>abs(current):
                    current=0
                elif abs(st[-1])<abs(current):
                    st.pop()
                else:
                    st.pop()
                    current=0
            if current!=0:
                st.append(current)
        return st
        