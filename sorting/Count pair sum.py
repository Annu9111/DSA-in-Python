# https://www.geeksforgeeks.org/problems/count-pair-sum5956/1?page=1&category=Hash,python&difficulty=Basic&sortBy=submissions
#User function Template for python3

class Solution:
    def countPairs(self,arr1, arr2, x):
        #code here.
        # count=0
        # for i in range(len(arr1)):
        #     for j in range(len(arr2)):
        #         if arr1[i]+arr2[j]==x:
        #             count+=1
        # return count 
        
        s=set(arr2)
        
        count=0
        for i in arr1:
            remaning=(x-i)
            if remaning in s:
                count+=1
        return count        
        
        
