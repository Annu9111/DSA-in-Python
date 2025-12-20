# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1?page=1&category=Sorting,python&sortBy=submissions
class Solution:
    def kthSmallest(self, arr, k):
        nums=sorted(arr)
        return nums[k-1]
        
