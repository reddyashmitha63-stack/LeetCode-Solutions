class MinStack(object):

    def __init__(self):
        self.stack=[]        
        self.mini=None
    def push(self, value):
        if not self.stack:
            self.mini=value
            self.stack.append(value)
            return
        if value>self.mini:
            self.stack.append(value)
        else:
            self.stack.append(2*value-self.mini)
            self.mini=value
        

    def pop(self):
        if not self.stack:
            return
        x=self.stack.pop()
        if x<self.mini:
            self.mini=2*self.mini-x
    def top(self):
        if not self.stack:
            return -1
        x=self.stack[-1]
        if x>self.mini:
            return x
        return self.mini
    def getMin(self):
        return self.mini
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()