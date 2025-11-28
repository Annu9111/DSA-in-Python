#question:https://www.geeksforgeeks.org/problems/find-length-of-loop/1
'''
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''

class Solution:
    def lengthOfLoop(self, head):
        slow=fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                count=1
                fast=fast.next
                while fast!=slow:
                    fast=fast.next
                    count+=1
                return count
        return 0        
        