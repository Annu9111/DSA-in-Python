#question:https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1
from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

class Solution:
    def findPairsWithGivenSum(self, target : int, head : Optional['Node']) -> List[List[int]]:
        #bruitfull solution
        temp1=head
        result=[]
        while temp1 is not None:
            temp2=temp1.next
            while temp2 is not None:
                if temp1.data+temp2.data==target:
                    result.append([temp1.data,temp2.data])
                temp2=temp2.next
            temp1=temp1.next
        return result 
        
        #better solution
        # myset=set()
        # temp=head
        # result=[]
        # while temp is not None:
        #     remaining=target-temp.data
        #     if remaining in myset:
        #         result.append([remaining,temp.data])
        #     myset.add(temp.data)
        #     temp=temp.next
        # return result  
        
        
        
    
        
