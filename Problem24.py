class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next:
            return head

        firstNode = head
        counter = 1
        previousNode = 0

        while head:
            if counter % 2 == 0:
                # swapping the values
                tempValue = head.val
                head.val = previousNode.val
                previousNode.val = tempValue

            previousNode = head
            head = head.next
            counter += 1
        return firstNode
