class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = [] # list of queues 
        nums_to_group = {}

        for n in sorted(nums):
            if not groups or abs(n-groups[-1][-1]) > limit:
                groups.append(deque())

            groups[-1].append(n)
            nums_to_group[n] = len(groups) - 1

        res = []
        for n in nums:
            j = nums_to_group[n]
            res.append(groups[j].popleft())

        return res


        