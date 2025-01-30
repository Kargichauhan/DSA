# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        0   1   2   3   4
        1   2   3   4   5

        n/2

        one direction -> more than one pointer 

        '''
        if head.next is None:
            return None
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        prev.next = prev.next.next
        return head
        




        