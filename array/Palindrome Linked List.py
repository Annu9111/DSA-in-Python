#question:https://leetcode.com/problems/palindrome-linked-list/description/?envType=problem-list-v2&envId=two-pointers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        ans=[]
        current=head
        while current:
            ans.append(current.val)
            current=current.next

        l,r=0,len(ans)-1
        while l<=r:
            if ans[l]!=ans[r]:
                return False
            l+=1
            r-=1    
        return True            
        