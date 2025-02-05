class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        """
        arr = [num]
        k

        arr[ans] -> size [n-k+1]
        ans[i] -> distinct numbers in subarray -> num[i:i + k -1]


        nums = [1,2,3,2,2,1,3], k = 3

        Output: [3,2,2,2,3]

        0: 2 = ans[0] = 3


        hash table

        sliding window

        TC:
        SC:


        """
        N = len(nums)

        ans = []

        window = collections.Counter()
        for right in range(N):

            window[nums[right]] += 1

            left = right - k

            if left >= 0:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]


            
                

            if left + 1 >= 0:
                # right + left with contain k element
                ans.append(len(window))
        return ans
