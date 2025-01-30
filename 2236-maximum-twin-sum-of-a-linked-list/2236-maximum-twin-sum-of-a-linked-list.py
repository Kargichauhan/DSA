# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        list = []
        curr = head 

        while curr:
            list.append(curr.val)
            curr = curr.next
        s, e, ans = 0, len(list) -1, 0
        while s < e:
            ans = max(ans, list[s] + list[e])
            s += 1
            e -= 1

        return ans
        