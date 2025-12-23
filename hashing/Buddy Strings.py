# https://leetcode.com/problems/buddy-strings/description/?envType=problem-list-v2&envId=hash-table
class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        diff=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                diff.append(i)
                if len(diff)>2:
                    return False
        return len(diff)==2 and s[diff[0]]==goal[diff[1]] and s[diff[1]]==goal[diff[0]]                    
        