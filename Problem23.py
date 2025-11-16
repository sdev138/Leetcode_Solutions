# defining ListNode class for
# testing purposes only
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
Solution class
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        head = point = ListNode(0)
        for list_ in lists:
            while list_:
                nodes.append(list_.val)
                list_ = list_.next

        for x in sorted(nodes):
            point.next = ListNode(x)
            point = point.next

        return head.next
