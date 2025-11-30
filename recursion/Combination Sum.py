#question:https://leetcode.com/problems/combination-sum/description/
class Solution(object):
    def solve(self,index,total,subset,nums,target,result):
        if total==target:
            result.append(subset[::])
            return
        elif total>target:
            return 
        if index>=len(nums):
            return
        subset.append(nums[index])
        sums=total+nums[index]
        self.solve(index,sums,subset,nums,target,result)
        sums= total
        subset.pop()
        self.solve(index+1,sums,subset,nums,target,result)           


    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result=[]
        candidates.sort()
        self.solve(0,0,[],candidates,target,result)
        return result

        