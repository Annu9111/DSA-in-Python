#question:https://leetcode.com/problems/divide-two-integers/
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return 2**31-1

        result=int(dividend/divisor)

        int_max=2**31-1
        int_min=-2**31
        if result<int_min:
            return int_min
        if result>int_max:
            return int_max
        return result        
        
        
