#Question:https://leetcode.com/problems/generate-parentheses/description/
class Solution(object):
    def solve(self,index,total,bracket,result):
        if index>=len(bracket):
            if total==0:
                result.append("".join(bracket))
            return
        if total>len(bracket)//2:
            return
        if total<0:
            return
        bracket[index]="("
        self.solve(index+1,total+1,bracket,result)
        bracket[index]=")"
        self.solve(index+1,total-1,bracket,result)        

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        bracket=[""]*(2*n)
        result=[]
        self.solve(0,0,bracket,result)
        return result
        