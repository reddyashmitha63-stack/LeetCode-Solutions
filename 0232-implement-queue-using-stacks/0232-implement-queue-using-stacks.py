class MyQueue(object):

    def __init__(self):
        self.input=[]
        self.output=[]
        

    def push(self, x):
        self.input.append(x)
        

    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return -1
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return -1
        return self.output[-1]

    def empty(self):
        return not self.input and not self.output


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()