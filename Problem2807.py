# math is already imported in leetcode
import math

# Both optional and listnode classes are implemented for testing purposes
class Optional:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # arguments are different to the real problem, you must fix for it to work
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        node1 = head
        node2 = head

        # iterating through the list node
        while node2:
            # finding the greatest divisor between two values
            gcdValue = math.gcd(node1.val, node2.val)
            gcdNode = ListNode(gcdValue)

            node1.next = gcdNode
            gcdNode.next = node2

            node1 = node2
            node2 = node2.next

        return head
