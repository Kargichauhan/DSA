class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        best_diag = -1
        best_area = 0 

        for [L,W] in dimensions:
            diag2 = L*L + W*W
            area  = L * W
            if diag2 > best_diag:
                best_diag = diag2
                best_area = area
            elif diag2 == best_diag and area > best_area:
                best_area = area

        return best_area





        

