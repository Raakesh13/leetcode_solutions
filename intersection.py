# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        elif (headA.next == None or headB.next == None) and headA != headB:
            return None
        else:
            count = 0
            currentA = headA
            currentB = headB
            while currentA != currentB:
                currentA = currentA.next
                currentB = currentB.next
                if currentA == None:
                    currentA = headB
                    count += 1
                if currentB == None:
                    currentB = headA
                    count += 1
                if count > 2:
                    return None
            return currentA


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    # l1.next.next = ListNode(5)
    # l1.next.next.next = ListNode(7)
    # l1.next.next.next.next = ListNode(9)
    # l1.next.next.next.next.next = ListNode(11)
    l2 = ListNode(3)
    l2.next = ListNode(4)
    # l2.next.next = l1.next.next

    ob = Solution()
    h = ob.getIntersectionNode(l1, l2)
    print(h.val)
