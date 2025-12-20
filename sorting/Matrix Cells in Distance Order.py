# https://leetcode.com/problems/matrix-cells-in-distance-order/description/?envType=problem-list-v2&envId=sorting
class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in range(rows):
            for j in range(cols):
                result.append([i,j])
        result.sort(key=lambda x:abs(x[0]-rCenter)+abs(x[1]-cCenter))
        return result
