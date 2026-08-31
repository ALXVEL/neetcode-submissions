# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def mergeTwoLists(head1, head2):
            dummy = ListNode(None, None)
            curr = dummy

            while head1 and head2:
                if head1.val < head2.val:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                
                curr = curr.next

            if head1:
                curr.next = head1
            else:
                curr.next = head2

            return dummy.next
        
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        else:
            merged_list = mergeTwoLists(lists[0], lists[1])
            for i in range(2, len(lists)):
                merged_list = mergeTwoLists(merged_list, lists[i])
            return merged_list
        
        return []
