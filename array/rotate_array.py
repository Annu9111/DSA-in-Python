#question:https://leetcode.com/problems/rotate-array/description/
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n=len(nums)
        # k=k%n
        # nums[:]=nums[-k:] + nums[:-k]

        n=len(nums)
        rotation=k%n
        for _ in range(0,rotation):
            e=nums.pop()
            nums.insert(0,e)

        # for i in range(0,k):
        #     a=nums.pop()
        #     nums.insert(0,a)
        # return nums    
        