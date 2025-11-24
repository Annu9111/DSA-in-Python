#question:https://leetcode.com/problems/missing-number/description/
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # a=sorted(nums)
        # for i in range(len(nums)):
        #     if i not in nums:
        #         return i
            
            
            
        n=len(nums)    
        return n*(n+1)//2 - sum(nums)    