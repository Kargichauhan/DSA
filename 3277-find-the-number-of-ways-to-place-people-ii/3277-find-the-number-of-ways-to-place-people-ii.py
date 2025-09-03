class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p:(p[0], -p[1]))
        n = len(points)
        ans = 0 

        for i in range(n):
            upper_y = points[i][1]
            best_lower_y = float("-inf")
            
            for j in range(i + 1, n):
                xj, yj = points[j]
                if yj <= upper_y and yj > best_lower_y:
                    ans += 1
                    best_lower_y = yj
                    if yj == upper_y:
                        break 

        return ans