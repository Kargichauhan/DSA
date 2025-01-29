from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)
        pairs = 0 


        rows = defaultdict(int)
        for row in grid:
            rows[tuple(row)] += 1

        for cols in range(n):
            column = tuple(grid[r][cols] for r in range(n))

            if column in rows:
                pairs += rows[column]

        return pairs

        
        
'''
        3122: 1
        1445: 1
        2422:2
        2422: 2

        pairs = 3 






        Sketch:
        n x n 
        ri = rows 
        cj = columns

        if same element and same order = return True

        pairs: 

        algo:

        Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
        Output: 1

        tc:

        sc:



        

        row = []
        col = []

        if len(row) != len(col):
            return False

        
        for i in len(row):
            if i in row:
                row.append(i)

            elif i in col:
                col.append(i)

            else: return False
        '''