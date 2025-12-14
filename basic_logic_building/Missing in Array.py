# https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?page=1&category=Arrays,Strings,Hash,Matrix,Linked%20List,Stack,Binary%20Search%20Tree,Queue,Map,python,Poin
class Solution:
    def missingNum(self, arr):
        # n=len(arr)
        # nums=sorted(arr)
        # for i in range(0,n-1):
        #     if nums[i+1]!=nums[i]+1:
        #         return nums[i]+1
        
        n=len(arr)+1
        totalsum=n*(n+1)//2
        return totalsum-sum(arr)
            