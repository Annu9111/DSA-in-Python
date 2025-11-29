#question:https://leetcode.com/problems/single-number/description/
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bruitful sol

        a={}
        for i in nums:
            if a.get(i):
                a[i]=a[i]+1
            else:
                a[i]=1
        for keys,values in a.items():
            if values==1:
                return keys    

        #optimal solution
        ans=0
        for i in nums:
            ans=ans^i
        return ans    

            
        
        
        