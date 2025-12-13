# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/?envType=problem-list-v2&envId=sorting
class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        return sorted(arr,key=lambda x:(bin(x).count("1"),x))
        