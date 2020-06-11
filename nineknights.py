import sys

board = [
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False]
    ]
moves = [[1,2], [-1,2], [1,-2], [-1,-2], [2,1], [2,-1], [-2,1], [-2,-1]]
c = 0

for i in range(5):
    line = input()
    c += line.count('k')
    for j in range(5):
        if (line[j] is "k"):
            x = j+2
            y = i+2
            board[x][y] = True

if (c!=9):
    print("invalid")
    sys.exit()

for i in range(5):
    for j in range(5):
        x = j+2
        y = i+2
        if (board[x][y]==True):
            for k in moves:
                if (board[x+k[0]][y+k[1]]==True):
                    print("invalid")
                    sys.exit()

print("valid")
sys.exit()