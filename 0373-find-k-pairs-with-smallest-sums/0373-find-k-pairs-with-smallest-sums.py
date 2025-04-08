class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        nums1 = [1,7,11]
        nums2 = [2,4,6]

        k = 3 

        [1,2],[1,4],[1,6],[7,2],[7,4],    [11,2],[7,6],[11,4],[11,6]
        [3]     [5]   [7]   [9]     [11]    [13]    [13]    [15]    [17]


        small sum : [3]     [5]   [7]


        min heap -> (nums1[i] + nums2[j], i,j)
        (nums1[0] + nums2[j], 0, j) => j from 0 to min(k, len(nums2))

        pop the heap k times: 
        (nums1[i+1], nums2[j]) -> if i + 1 is in bound
        '''
        if not nums1 or not nums2:
            return []

        min_heap = []
        res = []

        #initialize heap with pairs 
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        while min_heap and len(res) < k:
            curr_sum, i , j = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            #move to next element in nums1
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))


        return res

        
