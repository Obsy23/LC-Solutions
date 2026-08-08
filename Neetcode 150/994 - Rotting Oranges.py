'''
Runtime: 3ms (Beats 75%)
Memory: 19.36MB (Beats 41.27%)
'''

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        t=0
        freshOranges = 0
        queue = []
        visited = []

        #Create 2d array to track visits and no. fresh oranges
        for i in range(len(grid)):
            row = []
            for j in range(len(grid[0])):
                row.append(False)
                if (grid[i][j] == 1):
                    freshOranges += 1
                elif (grid[i][j] == 2):
                    queue.append(([i,j], t))
            visited.append(row)
        
        m = len(grid)
        n = len(grid[0])

        #edge cases
        if (freshOranges == 0):       
            return 0
        if (len(queue) == 0):           
            return -1

        #BFS
        while (queue):
            if (freshOranges == 0):
                break
            coords, time = queue.pop(0)
            i,j = coords
            if (visited[i][j] == True): 
                continue
            visited[i][j] = True
            if (grid[i][j] == 0):
                continue
            if (grid[i][j] == 1):
                grid[i][j] = 2
                freshOranges-=1
            if (i+1 < m):
                queue.append(((i+1, j), time+1))
            if (j+1 < n):
                queue.append(((i, j+1), time+1))
            if (i-1 >= 0):
                queue.append(((i-1, j), time+1))
            if (j-1 >= 0):
                queue.append(((i, j-1), time+1))
        if (freshOranges != 0):
            return -1
        return time