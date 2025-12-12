#question:https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1?page=1&category=Strings,python&difficulty=Easy&sortBy=submissions
#User function Template for python3
class Solution:
    def longestCommonPrefix(self, arr):
        arr=sorted(arr)
        first=arr[0]
        last=arr[-1]
        ans=""
        length=min(len(first),len(last))
        for i in range(length):
            if first[i]==last[i]:
                ans+=first[i]
            else:
                break
        return ans        
            