# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # if we put 1 node ahead of another by n + 1 (because we want the before node)

        dummy = ListNode(None, head)
        
        ptr1, ptr2 = dummy, dummy

        count = 0
        while count < n:
            ptr2 = ptr2.next
            count +=1
        
        while ptr2.next:
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr1.next = ptr1.next.next

        return dummy.next


