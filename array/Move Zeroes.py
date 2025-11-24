#question:https://leetcode.com/problems/move-zeroes/description/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]==0 and nums[j]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    i+=1
        return nums            