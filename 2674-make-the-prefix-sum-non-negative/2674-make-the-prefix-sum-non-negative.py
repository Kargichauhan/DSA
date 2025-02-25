class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        operations = 0
        prefix_sum = 0
        pq = []

        for num in nums:
            # Push negative elements to the min heap.
            if num < 0:
                heapq.heappush(pq, num)

            prefix_sum += num
            # Pop the minimum element from the heap and subtract from the sum.
            if prefix_sum < 0:
                prefix_sum -= heapq.heappop(pq)
                # Increment the operations required.
                operations += 1

        return operations
        