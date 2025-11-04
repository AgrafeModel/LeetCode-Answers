# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        stack = []

        temp = ListNode()
        temp.next = head

        previous = temp  # keep track the left node before the swap
        for i in range(left-1):
            previous = previous.next


        current = previous.next
        for i in range(right-left + 1):
            stack.append(current)
            current = current.next

        #unwind the stack
        while stack:
            previous.next = stack.pop()
            previous = previous.next

        previous.next = current

        return temp.next

