class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ''' 3 x 4
        12-> 6 = [6-1/3 , 6%4], [3-1/6 , 3%4] 1-1/6
        '''
        l = 0
        r = len(matrix) * len(matrix[0])
        rows = len(matrix)
        cols = len(matrix[0])
        while l < r:
            m = (l + r)//2
            if target == matrix[m // cols][m % cols]:
                return True
            elif target > matrix[m // cols][m % cols]:
                l = m + 1
            else:
                r = m
        return False



        