class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, visited, i, j):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0])):
                return 
            if(visited[i][j] == True):
                return 
            visited[i][j] = True
            dx = [-1,0,1,0]
            dy = [0,1,0,-1]
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if(x>=0 and x<len(grid) and y>=0 and y<len(grid[0]) and grid[x][y] == '1'):
                    dfs(grid, visited, x, y)
            
            return
        
        visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == '1' and visited[i][j] == False):
                    dfs(grid, visited, i, j)
                    cnt += 1
        
        return cnt