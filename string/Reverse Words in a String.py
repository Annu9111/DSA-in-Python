#Question:https://leetcode.com/problems/reverse-words-in-a-string/description/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split()
        b= a[::-1]
        return " ".join(b)
        