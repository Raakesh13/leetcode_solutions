# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            _next = head.next.next
            head.next.next = head
            head.next = _next
            self.swapPairs(head.next)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

ob = Solution()
print(ob.swapPairs(head))
