#question:https://www.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&category=Strings,python&sortBy=submissions
class Solution:
    def isBalanced(self, s):
        if s[0] in "}])":
            return False
            
        stack=[]
        pairs={"}":"{","]":"[",")":"("}
        for i in s:
            if i in "{[(":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1]==pairs[i]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0            

    

        
        