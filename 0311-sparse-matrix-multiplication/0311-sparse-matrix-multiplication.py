class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        m, k = len(mat1), len(mat1[0])
        k2, n = len(mat2), len(mat2[0])


        #santiy check 
        if k != k2:
            return []



        # all values start at 0
        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for x in range(k):
                if mat1[i][x] != 0:
                    #skip computation == sparse mat

                    for j in range(n):
                        if mat2[x][j] != 0:
                            res[i][j] += mat1[i][x] * mat2[x][j]

        return res       
        
        