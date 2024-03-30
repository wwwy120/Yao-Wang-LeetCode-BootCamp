class MyQueue(object):

    def __init__(self):
        self.store = []
        self.implement = []
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.store.append(x)
        self.length += 1
        

    def pop(self):
        """
        :rtype: int
        """
        for i in range(self.length):
            self.implement.append(self.store.pop())
        res = self.implement.pop()
        self.length -= 1
        for i in range(self.length):
            self.store.append(self.implement.pop())
        return res
        

    def peek(self):
        """
        :rtype: int
        """
        return self.store[0]

    def empty(self):
        """
        :rtype: bool
        """
        return self.length == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
