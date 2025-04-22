# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set = set(nums)
        count = 0
        node = head
        
        while node:
            # If current node is in nums, but either it's the last node
            # or the next node is NOT in nums, that's the end of a component.
            if node.val in nums_set and (not node.next or node.next.val not in nums_set):
                count += 1
            node = node.next
        
        return count

        