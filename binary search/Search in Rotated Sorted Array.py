#question:https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # n=len(nums)
        # lower_b=n
        # low,high=0,n-1
        # while low<=high:
        #     mid=(low+high)//2
        #     if nums[mid]>=target:
        #         lower_b=mid
        #         high=mid-1
        #     else:
        #         low=mid+1
        # if target not in nums:
        #     return -1
        # else: 
        #     return lower_b   

        # count=0
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i  
        # return -1  
        if target not in nums:
            return -1   

        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1

