#question:https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1
class Solution:
    def findFloor(self, arr, x):
        
        n=len(arr)
        lower_bound=-1
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=x:
                lower_bound=mid
                high=mid+1
            else:
                low=mid-1
        return lower_bound    
        
        
        
        
        