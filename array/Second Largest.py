#question:https://www.geeksforgeeks.org/problems/second-largest3735/1?page=1&sortBy=submissions
class Solution:
    def getSecondLargest(self, arr):
        largest=max(arr)
        s_largest=-1
        
        for i in range(len(arr)):
            if arr[i]!=largest:
                s_largest=max(s_largest,arr[i])
        return s_largest        
                