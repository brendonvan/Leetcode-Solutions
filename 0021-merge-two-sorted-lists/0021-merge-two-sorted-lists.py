# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:      
        # check each current head
        # if head is less than or equal to other
        # add to LinkedList and on that list assign .next to current node
        
        dummy = ListNode()
        res = dummy
        
        while (list1 and list2):
            
            if list1.val <= list2.val:
                res.next = list1
                print(res.val)
                list1 = list1.next
            else:
                res.next = list2
                print(res.val)
                list2 = list2.next 
                
            res = res.next
                
        if list1:
            res.next = list1
        elif list2:
            res.next = list2
            
        return dummy.next
                
#         dummy = ListNode()
#         tail = dummy

#         while list1 and list2:
#             if list1.val < list2.val:
#                 tail.next = list1
#                 list1 = list1.next
#             else:
#                 tail.next = list2
#                 list2 = list2.next
#             tail = tail.next

#         if list1:
#             tail.next = list1
#         elif list2:
#             tail.next = list2

#         return dummy.next