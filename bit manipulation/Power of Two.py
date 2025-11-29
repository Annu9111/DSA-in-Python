#question:https://leetcode.com/problems/power-of-two/description/class Solution(object):
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n>0 and (n & (n-1))==0:
            return True
        else:
            return False    

                

              