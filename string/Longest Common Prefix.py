#Question:https://leetcode.com/problems/longest-common-prefix/description/
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a=sorted(str)
        first=a[0]
        last=a[-1]
        length=min(len(first),len(last))
        ans=""
        for i in range(length):
            if first[i]==last[i]:
                ans+=i
            else:
                break
        return ans        
                
        
        