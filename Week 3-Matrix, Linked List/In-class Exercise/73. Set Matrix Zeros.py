class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        #Time Complexity: O(nm(n+m))
        #Space Complexity: O(1)
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    for c in range(len(matrix[0])):
                        if matrix[row][c] != 0:
                            matrix[row][c] = 2**31
                    for r in range(len(matrix)):
                        if matrix[r][column] != 0:
                            matrix[r][column] = 2**31

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 2**31:
                    matrix[row][column] = 0
        
        return
        




        #Time Complexity: O(mn)
        #Space Complexity: O(k), k is the numbers of zeroes
        zero = []
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    zero += [[row, column]]
        
        for idx in zero:
            for row in range(len(matrix)):
                for column in range(len(matrix[0])):
                    if row == idx[0] or column == idx[1]:
                        matrix[row][column] = 0
        
        return



