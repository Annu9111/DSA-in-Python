#question:https://www.geeksforgeeks.org/problems/implement-stack-using-array/1
class myStack:
    def __init__(self, n):
        self.n=n
        self.lst=[]

    
    def isEmpty(self):
        return len(self.lst)==0

    
    def isFull(self):
        return len(self.lst)==self.n

    
    def push(self, x):
        if len(self.lst)!=self.n:
            self.lst.append(x)

    
    def pop(self):
        if len(self.lst)!=0:
            return self.lst.pop()

    
    def peek(self):
        if len(self.lst)==0:
            return -1
        return self.lst[-1]