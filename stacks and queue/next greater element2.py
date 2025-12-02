#question:https://leetcode.com/problems/next-greater-element-ii/description/
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        stack=[]
        ans=[-1]*n
        for i in range(2*(n-1),-1,-1):
            while len(stack)!=0 and stack[-1]<=nums[i%n]:
                stack.pop()
            if i<n:
                if len(stack)!=0:
                    ans[i]=stack[-1]
            stack.append(nums[i%n])
        return ans            

        