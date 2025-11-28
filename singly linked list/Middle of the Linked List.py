#question:https://leetcode.com/problems/middle-of-the-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #Tortoise method
        slow=head
        fast=head
        while fast !=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        return slow    

        