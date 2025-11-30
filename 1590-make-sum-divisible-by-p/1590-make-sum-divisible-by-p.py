class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        # Already divisible?
        if target == 0:
            return 0
        
        n = len(nums)
        min_len = n  # worst case: remove all (but not allowed, so we'll check)
        
        # Hash map: prefix_mod_value -> latest index
        mod_index = {0: -1}  # prefix sum 0 at "index -1"
        prefix = 0
        
        for j in range(n):
            prefix = (prefix + nums[j]) % p
            
            # We want a previous prefix such that:
            # (prefix - prev_prefix) % p == target
            # → prev_prefix ≡ (prefix - target) mod p
            needed = (prefix - target) % p
            
            if needed in mod_index:
                i = mod_index[needed]
                length = j - i  # subarray from i+1 to j
                if length < n:  # can't remove whole array
                    min_len = min(min_len, length)
            
            # Update map: keep latest index for this mod value
            mod_index[prefix] = j
        
        return min_len if min_len < n else -1