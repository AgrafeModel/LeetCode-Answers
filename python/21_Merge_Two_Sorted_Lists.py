# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        r = root
        while list1 is not None and list2 is not None:
            r.next = ListNode()
            if list1 is not None and list1.val <= list2.val:
                r.next.val = list1.val
                list1 = list1.next
            elif list2 is not None and list2.val < list1.val:
                r.next.val = list2.val
                list2 = list2.next
 
            r = r.next

        while list1 is not None:
            r.next = ListNode(list1.val)
            list1=list1.next
            r = r.next
    
        while list2 is not None:
            r.next = ListNode(list2.val)
            list2=list2.next
            r = r.next

        return root.next
