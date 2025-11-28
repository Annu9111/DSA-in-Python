#question :https://leetcode.com/problems/reverse-linked-list/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # stack=[]
        # current=head
        # while current is not None:
        #     stack.append(current.val)
        #     current=current.next

        # current=head
        # while current is not None:
        #     e=stack.pop()
        #     current.val=e
        #     current=current.next  
        # return head    

        current=head
        prev=None
        while current!=None:
            front=current.next
            current.next=prev
            prev=current
            current=front
        return prev    

        