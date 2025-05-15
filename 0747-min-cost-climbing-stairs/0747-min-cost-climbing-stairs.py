class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1) Append a "0" cost for the top beyond the last step.
        #    This lets us treat the top as just another step with zero cost.
        cost.append(0)

        # 2) Fill in cost[i] = min total cost to reach the top starting from i.
        #    We work backwards from the step just before the top (len(cost)-3)
        #    down to step 0.
        for i in range(len(cost) - 3, -1, -1):
            # At each step i, you can go either to i+1 or i+2.
            # So the min cost from i is:
            #   original cost at i  +  min(cost[i+1], cost[i+2])
            cost[i] += min(cost[i+1], cost[i+2])

        # 3) You can start the climb at step 0 or step 1,
        #    so the answer is the cheaper of those two.
        return min(cost[0], cost[1])
        