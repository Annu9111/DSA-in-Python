#question:https://leetcode.com/problems/count-square-sum-triples/description/?envType=daily-question&envId=2025-12-08
class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        for i in range(1,n+1):
            for j in range(1,n+1):
                k=int((i*i +j*j)**0.5)
                if k*k==j*j+i*i and k<=n:
                    count+=1
        return count 

        