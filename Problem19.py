class Optional:
    pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        pass


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # checking if the head exists or if its a single node
        if not head or (head.next == None and n == 1):
            return []

        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first is not None:
            length += 1
            first = first.next
        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next
        first.next = first.next.next
        
        # returning the node next to the head
        return dummy.next
