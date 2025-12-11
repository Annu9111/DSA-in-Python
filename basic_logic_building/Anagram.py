#question:https://www.geeksforgeeks.org/problems/anagram-1587115620/1?page=1&category=Strings,python&sortBy=submissions
class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       return sorted(list(s1))==sorted(list(s2))
       