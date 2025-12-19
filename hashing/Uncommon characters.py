# https://www.geeksforgeeks.org/problems/uncommon-characters4932/1?page=1&category=Hash,python&difficulty=Basic&sortBy=submissions
#User function Template for python3

class Solution:
    # Function to find uncommon characters between two strings.
    def uncommonChars(self, s1, s2):
        set1=set(s1)
        set2=set(s2)
        uncommon=(set1-set2)|(set2-set1)
        return "".join(sorted(uncommon))
        
        