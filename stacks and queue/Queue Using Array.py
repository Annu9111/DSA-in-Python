#question:https://www.geeksforgeeks.org/problems/implement-queue-using-array/1
class myQueue:
    def __init__(self, n):
        self.n=n
        self.lst=[]

    
    def isEmpty(self):
        return len(self.lst)==0

    
    def isFull(self):
        return len(self.lst)==self.n

    
    def enqueue(self, x):
        if self.isFull():
            return 
        self.lst.append(x)
        

    
    def dequeue(self):
        if self.isEmpty():
            return 
        a=self.lst.pop(0)
        return a

    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.lst[0]
       
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.lst[-1]
        
        