#question:https://leetcode.com/problems/ugly-number/description/?envType=problem-list-v2&envId=math
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n//=i
        return n==1

        