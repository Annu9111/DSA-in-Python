#question:https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=hash-table
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p1=headA
        p2=headB
        while p1!=p2:
            p1=p1.next if p1 else headB
            p2=p2.next if p2 else headA
        return p1        
            
        