#question:https://leetcode.com/problems/two-sum/description/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        a={}
        for i in range(0,n):
            remain=target-nums[i]
            if remain in a:
                return [a[remain],i]
            a[nums[i]]=i