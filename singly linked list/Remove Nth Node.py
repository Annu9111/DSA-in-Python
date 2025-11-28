#question:https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        #bruitful sol
        # length=0
        # temp=head
        # while temp is not None:
        #     length+=1
        #     temp=temp.next
        # if length==n:
        #     new_head=head
        #     del head
        #     return new_head
        # temp=head
        # pos_to_stop=length-n
        # count=1
        # while count<pos_to_stop:
        #     count+=1
        #     temp=temp.next
        # temp.next=temp.next.next
        # return head            


        #optimal sol
        slow=fast=head
        for _ in range(n):
            fast=fast.next

        if fast==None:
            return head.next

        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head            