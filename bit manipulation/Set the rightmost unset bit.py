#question:https://www.geeksforgeeks.org/problems/set-the-rightmost-unset-bit4436/1
#User function Template for python3
class Solution:
	def setBit(self, n):
	    if n>=0 and n-1>=0:
		    return (n | (n-1))