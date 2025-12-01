#question:https://www.geeksforgeeks.org/problems/implement-stack-using-linked-list/1
# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None 


# Stack class template
class myStack:

    def __init__(self):
        self.head=None
        self.tail=None
        

    def isEmpty(self):
        return self.head==None and self.tail==None
        

    def push(self, x):
        new_node=Node(x)
        if self.head is None and self.tail is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        

    def pop(self):
        if self.isEmpty():
            return -1
        if self.head==self.tail:
            pop_value=self.head.data
            self.head=self.tail=None
        else:
            temp=self.head
            while temp.next!=self.tail:
                temp=temp.next
            pop_value=self.tail.data
            temp.next=None
            self.tail=temp
        return pop_value    
            
        


    def peek(self):
        if self.head is None and self.tail is None:
            return -1
        return self.tail.data    


    def size(self):
        if self.head is None and self.tail is None:
            return 0
        count=0
        temp=self.head
        while temp:
            count+=1
            temp=temp.next
        return count    