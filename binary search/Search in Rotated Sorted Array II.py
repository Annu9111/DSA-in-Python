#Question:https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return True
        # return False   

    
        n=len(nums)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                return True

            if nums[low]==nums[mid]==nums[high]:
                low+=1
                high-=1
                continue    

            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1

            else:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1

        return False                                     
        