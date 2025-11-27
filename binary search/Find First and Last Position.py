#question:https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
class Solution(object):
    def lower_bound(self,target,nums):
        n=len(nums)
        low,high=0,n-1
        lower_b=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                lower_b=mid
                high=mid-1
            else:
                low=mid+1    
        return lower_b

    def upper_bound(self,target,nums):
        n=len(nums)
        low,high=0,n-1
        upper_b=n
        while low<=high:
            mid=(low+high)//2
            if nums[mid]>target:
                upper_b=mid
                high=mid-1
            else:
                low=mid+1 
        return upper_b           

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """   
        lb=self.lower_bound(target,nums)
        up=self.upper_bound(target,nums)

        if lb==len(nums) or nums[lb]!=target:
            return [-1,-1]

        return [lb,up-1]    



        