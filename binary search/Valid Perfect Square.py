# https://leetcode.com/problems/valid-perfect-square/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low,high=0,num
        while low<=high:
            mid=(low+high)//2
            if mid*mid==num:
                return True
            elif mid*mid>num:
                high=mid-1
            else:
                low=mid+1
        return False        
