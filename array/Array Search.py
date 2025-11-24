#question:https://www.geeksforgeeks.org/problems/search-an-element-in-an-array-1587115621/1
class Solution:
    def search(self, arr, x):
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1  