# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        else:
            temp = ListNode(0)
            prev = temp
            prev.next = None

            while head != None:
                while prev.next != None and prev.next.val < head.val:
                    prev = prev.next

                _next = head.next
                head.next = prev.next
                prev.next = head
                prev = temp
                head = _next

        return temp.next


root = ListNode(9)
root.next = ListNode(5)
root.next.next = ListNode(10)
root.next.next.next = ListNode(6)
root.next.next.next.next = ListNode(3)
root.next.next.next.next.next = ListNode(2)

ob = Solution()
ob.insertionSortList(root)
