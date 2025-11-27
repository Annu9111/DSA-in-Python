#Question:https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mini=nums[0]
        # for i in range(len(nums)):
        #     a=nums[i]
        #     mini=min(mini,a)
        # return mini   


        n=len(nums)
        low,high=0,n-1
        mini=float("inf")

        while low<=high:
            mid=(low+high)//2
            if nums[mid]<=nums[high]:
                mini=min(mini,nums[mid])
                high=mid-1
            else:
                mini=min(mini,nums[low])  
                low=mid+1
        return mini          








