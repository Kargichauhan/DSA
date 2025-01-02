class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        n = len(nums)
        max_length = 0 
        left = 0 


        min_dq = deque()
        max_dq = deque()


        for right in range(n):
            while min_dq and nums[min_dq[-1]] >= nums[right]:
                min_dq.pop()

            while max_dq and nums[max_dq[-1]] <= nums[right]:
                max_dq.pop()



            min_dq.append(right)
            max_dq.append(right)


            while nums[max_dq[0]] - nums[min_dq[0]] >limit:
                left += 1
                if max_dq[0] < left:
                    max_dq.popleft()

                if min_dq[0] < left:
                    min_dq.popleft()



            max_length = max(max_length, right - left + 1)

        return max_length


            


            

        