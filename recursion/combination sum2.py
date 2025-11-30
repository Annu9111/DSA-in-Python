#Question:https://leetcode.com/problems/combination-sum-ii/description/
class Solution(object):
    def solve(self,index,total,subset,target,nums,result):
        if total==target:
            result.append(subset[::])
            return
        elif total>target:
            return
        if index>=len(nums):
            return
        subset.append(nums[index])
        self.solve(index+1,total+nums[index],subset,target,nums,result)
        subset.pop()
        self.solve(index+1,total,subset,target,nums,result)            


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        self.solve(0,0,[],target,candidates,result)
        a=[]
        for i in result:
            if i not in a:
                a.append(i)
        return a        
            
        