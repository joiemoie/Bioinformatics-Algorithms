def findEditDistance(a,b):
    grid = [[]]
    for i in range(len(a)+1):
        grid[0].append(i)
    for i in range(1,len(b)+1):
        for j in range(len(a)+1):
            if j == 0:
                grid.append([i])
            else:
                topLeft = grid[i-1][j-1]
                top = grid[i-1][j]
                left = grid[i][j-1]
                if(a[j-1]==b[i-1]):
                    grid[i].append(min(topLeft,top+1,left+1))
                else: grid[i].append(min(topLeft+1,top+1,left+1))
    return min(grid[len(b)])
