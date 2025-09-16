class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            if p < min_price:
                min_price = p          # buy cheaper if we can
            elif p - min_price > max_profit:
                max_profit = p - min_price  # sell today if better
        return max_profit
