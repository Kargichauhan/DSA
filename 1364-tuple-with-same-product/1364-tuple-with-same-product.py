class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prodt_cnt = defaultdict(int)
        pair_cnt = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                product = nums[i] * nums[j]
                pair_cnt[product] += prodt_cnt[product]
                prodt_cnt[product] += 1


        res = 0 

        for cnt in pair_cnt.values():
            res += 8*cnt
        return res
        
        