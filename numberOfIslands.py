class Solution:
    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        else:
            gridCount = 0
            m = len(grid)
            for i in range(m):
                n = len(grid[i])
                for j in range(n):
                    if grid[i][j] == "1":
                        gridCount += self.islandCount(grid, i, j)

            return gridCount

    def islandCount(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == "0":
            return 0

        grid[i][j] = "0"

        self.islandCount(grid, i-1, j)
        self.islandCount(grid, i+1, j)
        self.islandCount(grid, i, j-1)
        self.islandCount(grid, i, j+1)

        return 1


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]

ob = Solution()
print(ob.numIslands(grid))
