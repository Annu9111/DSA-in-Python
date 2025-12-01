#question:https://leetcode.com/problems/combination-sum-iii/
class Solution(object):
    def solve(self,index,total,subset,k,n,result,nums):
        if total==n and len(subset)==k:
            result.append(subset[::])
            return
        if index>=len(nums):h
            return    
        subset.append(nums[index])
        self.solve(index+1,total+nums[index],subset,k,n,result,nums)
        subset.pop()
        self.solve(index+1,total,subset,k,n,result,nums)        


    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        nums=[1,2,3,4,5,6,7,8,9]
        self.solve(0,0,[],k,n,result,nums)
        return result
        