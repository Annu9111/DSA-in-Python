#question:https://leetcode.com/problems/longest-palindrome/description/?envType=problem-list-v2&envId=hash-table
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==1:
            return 1
        my_dict={}
        for i in range(len(s)):
            my_dict[s[i]]=my_dict.get(s[i],0)+1

        count=0  
        found=False  

        for i in my_dict.values():
            if i%2 !=0:
                found=True
                count+=(i-1)
            else:
                count+=i
        if found:
            return count+1
        else:
            return count            

        