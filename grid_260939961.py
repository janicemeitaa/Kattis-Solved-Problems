from sys import stdin

def BFS(grid, n, m):
    visited = []
    
    for i in range(n * m):
        visited.append(False)
    visited[0] = True
    
    nxt = []
    move = [0, 0, 0]

    nxt.append(move)

    while (len(nxt)>0):
        
        current = nxt.pop(0)
        
        r = int(current[0])
        c = int(current[1])
        count = int(current[2])
        thisJump = grid[r+(c*n)]
        
        if (r == n-1) and (c == m-1):
            return count
        else:
            moveDown = r+thisJump
            moveUp = r-thisJump
            moveRight = c+thisJump
            moveLeft = c-thisJump
    
            if (moveDown < n) and (not (visited[moveDown+(c*n)])):
                nxt.append([moveDown, c, count+1])
                visited[moveDown+(c*n)] = True
            
            if (moveUp >= 0) and (not (visited[moveUp+(c*n)])):
                nxt.append([moveUp, c, count+1])
                visited[moveUp+(c*n)] = True
            
            if (moveRight < m) and (not (visited[r+(moveRight*n)])):
                nxt.append([r, moveRight, count+1])
                visited[r+(moveRight*n)] = True
            
            if (moveLeft >= 0) and (not (visited[r+(moveLeft*n)])):
                nxt.append([r, moveLeft, count+1])
                visited[r+(moveLeft*n)] = True
                
    return -1


inp = list(stdin.readline().split())

n = int(inp[0])
m = int(inp[1])

gridArray = []

for i in range(n):
    digit = stdin.readline().strip()
    for j in range(m):
        tmp = int(digit[j])
        gridArray.append(tmp)

print(BFS(gridArray, m, n))