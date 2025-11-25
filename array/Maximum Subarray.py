#question:https://leetcode.com/problems/maximum-subarray/description/
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #bruitful solution
        n=len(nums)
        maxi=float("-inf")
        total=0
        for i in range(0,n):
            total=0
            for j in range(i+1,n):
                total+=nums[j]
                maxi=max(maxi,total)
        return maxi
    
    #optimal solution
        n=len(nums)
        maxi=float("-inf")
        total=0
        for i in range(0,n):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi
                    