#Question:https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/0
#User function Template for python3

class Solution:
    def solve(self,nums,k,total,subset,index):
        if total==k:
            return True
        elif total>k:
            return False
        if index>=len(nums):
            return False
            
        subset.append(nums[index])
        pick=self.solve(nums,k,total+nums[index],subset,index+1)
        if pick:
            return True
        subset.pop()
        unpick=self.solve(nums,k,total,subset,index+1)
        return unpick
    
    
    
    
    def checkSubsequenceSum(self, N, arr, K):
        return self.solve(arr,K,0,[],0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    
        
         
                                                                                             