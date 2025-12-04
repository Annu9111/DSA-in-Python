#question:https://leetcode.com/problems/minimum-absolute-difference/description/?envType=problem-list-v2&envId=sorting
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        mini=float("inf")
        arr=sorted(arr)
        n=len(arr)
        count=0
        for i in range(0,n-1):
            count=arr[i+1]-arr[i]
            mini=min(count,mini)

        result=[]
    
        for i in range(0,n-1):
            if arr[i+1]-arr[i]==mini:
                result.append([arr[i],arr[i+1]])            
        return result            
