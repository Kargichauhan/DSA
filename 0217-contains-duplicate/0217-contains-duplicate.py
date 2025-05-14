class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = set(nums)

        return len(hashmap) != len(nums)

        