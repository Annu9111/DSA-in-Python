#question:https://leetcode.com/problems/subsets/description/
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        def solve(indx,sub):
            if indx>=len(nums):
                result.append(sub[:])
                return 
            sub.append(nums[indx])
            solve(indx+1,sub)
            sub.pop()
            solve(indx+1,sub)

        solve(0,[])   
        return result     
        