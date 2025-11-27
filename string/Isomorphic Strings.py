#Question:https://leetcode.com/problems/isomorphic-strings/description/
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=list(s)
        b=list(t)
        d=dict(zip(a,b))
        for i in t:
            if i not in d.values():
                return False
        return True