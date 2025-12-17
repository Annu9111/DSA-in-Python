# https://www.geeksforgeeks.org/problems/check-for-binary/1?page=1&category=Strings,python&difficulty=Basic&sortBy=submissions
# Return true if s is binary, else false
class Solution:
    def isBinary(self, s):
        for i in s:
            if i not in "10":
                return False
        return True        
                