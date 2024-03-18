class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #1. Transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        #2. Reverse rows
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]
        return
