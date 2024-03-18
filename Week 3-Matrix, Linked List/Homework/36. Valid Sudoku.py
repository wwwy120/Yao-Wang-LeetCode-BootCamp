class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Brute Force Approach
        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        #Check rows and columns
        for i in range(9):
            d_row = {}
            d_col = {}
            for j in range(9):
                if board[i][j] != ".":
                    if d_row.get(board[i][j], 0) == 1:
                        return False
                    d_row[board[i][j]] = d_row.get(board[i][j], 0) + 1
                if board[j][i] != ".":
                    if d_col.get(board[j][i], 0) == 1:
                        return False
                    d_col[board[j][i]] = d_col.get(board[j][i], 0) + 1
        
        #Check sub-boxes
        for i in range(3):
            for j in range(3):
                d = {}
                for ik in range(3):
                    for jk in range(3):
                        if board[3*i + ik][3*j + jk] != ".":
                            if d.get(board[3*i + ik][3*j + jk], 0) == 1:
                                return False
                            d[board[3*i + ik][3*j + jk]] = d.get(board[3*i + ik][3*j + jk], 0) + 1

        

        return True
