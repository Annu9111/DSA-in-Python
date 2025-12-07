#question:https://leetcode.com/problems/power-of-four/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n%4==0:
            n=n //4
        return n==1                 
        