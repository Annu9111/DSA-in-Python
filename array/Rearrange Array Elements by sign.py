#question:https://leetcode.com/problems/rearrange-array-elements-by-sign/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        neg=[]
        pos=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        
        for i in range(len(nums)):
            nums[2*i]=pos[i]
            nums[(2*i)+1]=neg[i]
        return nums              