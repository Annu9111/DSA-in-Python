#question:https://www.geeksforgeeks.org/problems/implement-queue-using-linked-list/1
# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        self.head=None
        self.tail=None
        

    def isEmpty(self):
        return self.head==None and self.tail==None
        

    def enqueue(self, x):
        new_node=Node(x)
        if self.isEmpty():
            self.head=self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
            
        
        

    def dequeue(self):
        if self.isEmpty():
            return -1
        pop_value=self.head.data
        self.head=self.head.next
        if self.head is None:
            self.tail=None
        return pop_value    


    def getFront(self):
        if self.isEmpty():
            return -1
        return self.head.data


    def size(self):
        if self.isEmpty():
            return 0
        temp=self.head
        count=0
        while temp is not None:
            count+=1
            temp=temp.next
        return count    
