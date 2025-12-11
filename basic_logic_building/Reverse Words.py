#question:https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1?page=1&category=Strings,python&sortBy=submissions
class Solution:
    def reverseWords(self, s):
        words=[w for w in s.split(".") if w]
        words.reverse()
        return ".".join(words)
        