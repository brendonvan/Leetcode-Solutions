class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy = [0,1,2,3,4,5]
        dummy = ListNode(0, head)
        
        # left = [0,1,2,3,4,5]
        left = dummy
        # right = [1,2,3,4,5]
        right = head

        while n > 0:
            # right = [3,4,5]
            right = right.next
            n -= 1

        while right:
            # left = [2,3,4,5]
            left = left.next
            # right = [4,5]
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next
