#question:https://leetcode.com/problems/linked-list-cycle-ii/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #bruitfull solution

        # count=0
        # current=head
        # dic={}
        # while current is not None:
        #     if current in dic:
        #         return current
        #     dic[current]=count
        #     count+=1
        #     current=current.next
        # return None       
        #-----------------------------------------------------------------

        #optimal solution
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None            