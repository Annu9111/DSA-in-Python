#question:https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1
#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
    	def solve(index,total):
            if total==target:
    	        return 1
    	    if total>target:
    	        return 0
    	    if index>=len(arr):
    	        return 0
    	    pick=solve(index+1,total+arr[index])
    	    unpick=solve(index+1,total)
    	    return pick+unpick
        return solve(0,0)  
	            
	            
		        