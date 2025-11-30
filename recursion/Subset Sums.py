#question:https://www.geeksforgeeks.org/problems/subset-sums2234/1
class Solution:
	def subsetSums(self, arr):
		result=[]
		def solve(index,subset):
		    if index>=len(arr):
		        result.append(sum(subset[:]))
		        return
		    subset.append(arr[index])
		    solve(index+1,subset)
		    subset.pop()
		    solve(index+1,subset)
	    solve(0,[])	 
	    return result