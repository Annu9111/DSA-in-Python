# https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        n=len(nums)
        j=n//2
        i=0
        result=[]
        while j<n:
            result.append(nums[i])
            result.append(nums[j])
            i+=1
            j+=1
        return result    

        