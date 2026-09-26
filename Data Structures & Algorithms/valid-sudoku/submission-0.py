class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def checkBox(board,l,k):
            found = {}
            for i in range(0,3):
                for j in range(0,3):
                    if board[3*l+i][3*k+j].isnumeric() and board[3*l+i][3*k+j] in found :
                        return False
                    elif board[3*l+i][3*k+j].isnumeric():
                        found[board[3*l+i][3*k+j]] = 1
            return True
        
        def checkRow(board, l):
            found = {}
            for i in range(0,9):
                if board[l][i].isnumeric() and board[l][i] in found:
                    return False
                elif board[l][i].isnumeric():
                        found[board[l][i]] = 1
            return True

        def checkCol(board, l):
            found = {}
            for i in range(0,9):
                if board[i][l].isnumeric() and board[i][l] in found:
                    return False
                elif board[i][l].isnumeric():
                        found[board[i][l]] = 1
            return True

        for i in range(0,3):
            for j in range(0,3):
                k = checkBox(board, i, j)
                if not k:
                    return False
        for i in range(0,9):
            k = checkRow(board, i)
            if not k:
                return False
            m = checkCol(board, i)
            if not m:
                return False

        return True



        
        