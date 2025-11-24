#question : https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
class Solution:
    def isSorted(self, arr) -> bool:
        for i in range(len(arr)-1):
            if arr[i+1]<arr[i]:
                return False
        return True  
      