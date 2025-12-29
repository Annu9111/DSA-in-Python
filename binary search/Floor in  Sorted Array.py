# https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1?page=1&category=Sorting,python&sortBy=submissions
class Solution:
    def findFloor(self, arr, x):
        # code here
        low=0
        high=len(arr)-1
        floor=-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]<=x:
                floor=mid
                low=mid+1
            else:
                high=mid-1
        return floor        
                
        