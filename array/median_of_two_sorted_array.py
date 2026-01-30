# question:https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=problem-list-v2&envId=array
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i,j=0,0
        n,m=len(nums1),len(nums2)
        result=[]

        while i<n and j<m:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1

        if i<n:
            while i<n:
                result.append(nums1[i])
                i+=1
        if j<m:
            while j<m:
                result.append(nums2[j])
                j+=1

        length=n+m
        if length%2!=0:
            return result[length//2]
        else:
            a1=result[length//2]
            a2=result[(length//2)-1]
            return (a1+a2)/2.0                                
                                   
                                       



        