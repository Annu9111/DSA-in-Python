#question:https://leetcode.com/problems/linked-list-cycle/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #brutfull solution

        current=head
        my_set=set()
        while current is not None:
            if current in my_set:
                return True
            my_set.add(current)
            current=current.next
        return False  

        #--------------------------------------------------------------------------------- 

        #optimal solution

        slow=head
        fast=head
        while fast !=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if fast==slow:
                return True
        return False                   
        