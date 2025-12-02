#question:https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # my_dict={}
        # left=0
        # right=0
        # maxi=0
        # while right<len(s):
        #     if s[right] in my_dict:
        #         left=max(left,my_dict[s[right]]+1)
        #     maxi=max(maxi,right-left+1)
        #     my_dict[s[right]]=right
        #     right+=1
        # return maxi   

        n=len(s)
        maxi=0
        for i in range(0,n):
            my_set=set()
            for j in range(i,n):
                if s[j] in my_set:
                    break
                maxi=max(maxi,j-i+1)
                my_set.add(s[j])
        return maxi            

              
              

        