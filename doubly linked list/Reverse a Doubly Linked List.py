#question:https://www.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        current=head
        while current!=None:
            current=current.next  
        while current:
            print(current.prev,end="")
            current=current.prev 
               