class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        used = [False] * len(baskets)
        unplaced_count = 0 

        for fruit_qty in fruits:
            placed = False
            for i in range(len(baskets)):
                if not used[i] and baskets[i] >= fruit_qty:
                    used[i] = True
                    placed = True
                    break 

            if not placed:
                unplaced_count += 1

        return unplaced_count
        