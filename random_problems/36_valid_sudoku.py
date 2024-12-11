# Test cases
board_0 = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

# Expected output: True

def isValidSudoku(board) -> bool:
    columns = []
    for _ in range(9):
        col = [0] * 9
        columns.append(col)
    print(columns)
    def isValidQuadrant(column, row, position):
        quadrant = []
        for quadrant_index in range(9):
            for _ in range(9): 
                quadrant.append()


isValidSudoku(board_0)

