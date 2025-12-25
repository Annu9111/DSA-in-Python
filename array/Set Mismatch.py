# https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """   
        c=[]
        a={}
        for i in nums:
            if a.get(i):
                a[i]=a[i]+1
            else:
                a[i]=1
        for keys,values in a.items():
            if values==2:
                c.append(keys)            
        for i in range(1,len(nums)+1):
            if i not in nums:
                c.append(i)            
        return c                     
        