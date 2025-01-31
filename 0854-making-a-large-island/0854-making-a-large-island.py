class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                grid[i][j] = id_island
                return dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1) + 1
            return 0

        m, n = len(grid), len(grid[0])
        id_island, dic_areas = 2, {}
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 1:
                dic_areas[id_island] = dfs(i, j)
                id_island += 1
                
        total_area = max(dic_areas.values(), default = 0)
        for i, j in product(range(m), range(n)):
            if grid[i][j] == 0:
                area, visited_island = 1, set()
                for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] > 0 and grid[ii][jj] not in visited_island:
                        area += dic_areas[grid[ii][jj]]
                        visited_island.add(grid[ii][jj])    
                total_area = max(area, total_area)
        return total_area
    