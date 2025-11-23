#question: https://www.geeksforgeeks.org/problems/merge-sort/1
class Solution: 
    def merge_arry(self,left,right):
        result=[]
        m,n=len|(left),len(right)
        i,j=0,0
        while i<m and j<n:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i<m:
            while i<m:
                result.append(left[i])
                i+=1
        if j<n:
            while j<n:
                result.append(right[j])
                j+=1
                
    def merge_sort(self,arry):
        if len(arry)==1:
            return arry
        mid=len(arry)//2
        left_arry=arry[:mid]
        right_arry=arry[mid:]
        left=self.merge_sort(left_arry)
        right=self.merge_sort(right_arry)
        return self.merge_arry(left,right)
                                        