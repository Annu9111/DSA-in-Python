# https://leetcode.com/problems/count-good-triplets/description/?envType=problem-list-v2&envId=enumeration
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans=0
        n=len(arr)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        ans+=1
        return ans            


        