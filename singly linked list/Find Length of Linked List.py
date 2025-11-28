#question: https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/0
'''
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
'''
class Solution:
    def getCount(self, head):
        count=0
        temp=head
        while temp!=None:
            count+=1
            temp=temp.next  
        return count    