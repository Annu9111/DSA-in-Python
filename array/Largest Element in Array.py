#question :https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0
class Solution:
    def largest(self, arr):
        largest=float("-inf")
        for i in arr:
            largest=max(largest,i)
        return largest    