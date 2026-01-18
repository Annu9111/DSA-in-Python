# https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1?page=1&sortBy=submissions
class Solution:
    def maxSubarraySum(self, arr):
        curr_sum=arr[0]
        max_sum=arr[0]
        for i in range(1,len(arr)):
            curr_sum=max(arr[i],curr_sum + arr[i])
            max_sum=max(max_sum,curr_sum)
        return max_sum    