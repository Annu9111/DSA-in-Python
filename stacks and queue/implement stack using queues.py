#question:https://leetcode.com/problems/implement-stack-using-queues/description/
from collections import deque
class MyStack(object):

    def __init__(self):
        self.queue=deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.append(x)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft())
        

    def pop(self):
        """
        :rtype: int
        """
        if len(self.queue)==0:
            return
        return self.queue.popleft()    
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.queue)==0:
            return
        return self.queue[0]    
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()