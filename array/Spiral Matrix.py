#question:https://leetcode.com/problems/spiral-matrix/description/
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix)
        left,top=0,0
        right,bottom=len(matrix)-1,len(matrix)-1
        result=[]
        
        while top<bottom and left<right:
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top+=1
            
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right-=1
            
            if top<=bottom:
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
            bottom-=1
            
            if left<=right:
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
            left+=1
            
        return result                       