# https://leetcode.com/problems/shortest-distance-to-a-character/description/?envType=problem-list-v2&envId=two-pointers
class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        n=len(s)
        result=[float("inf")]*n

        prev=float("-inf")
        for i in range(n):
            if s[i]==c:
                prev=i
            result[i]=i-prev

        prev=float("inf")
        for i in range(n-1,-1,-1):
            if s[i]==c:
                prev=i
            result[i]=min(result[i],prev-i)
        return result                
        