class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        def findLeft():
            left = 0
            right = n - 1
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        
        def findRight():
            left = 0
            right = n - 1
            index = -1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        index = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return index
        leftIndex = findLeft()
        if leftIndex == -1:
            return [-1, -1]
        rightIndex = findRight()
        return [leftIndex, rightIndex]        