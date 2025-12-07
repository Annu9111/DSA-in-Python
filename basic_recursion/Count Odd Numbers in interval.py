#question:https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/?envType=daily-question&envId=2025-12-07
class Solution(object):
    def countOdds(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        length=high-low+1
        count=length//2
        if length%2 and low%2:
            count+=1
        return count       

                                
        