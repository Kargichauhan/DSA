class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        for current_box in range(len(boxes)):
            if boxes[current_box] == '1':
                for new_pos in range(len(boxes)):
                    ans[new_pos] += abs(new_pos - current_box)

        return ans

        