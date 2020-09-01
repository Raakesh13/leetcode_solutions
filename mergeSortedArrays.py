# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    if l1.val <= l2.val:
        l = l1
    else:
        l = l2
    temp = None
    flag = 0
    while l1 != None or l2 != None:

        if l1.val <= l2.val:
            if flag == 1:
                temp = None
            else:
                temp = l1.next
            l1.next = l2
            l2 = l1
            l1 = temp
            if l1.next == None:
            flag = 1
            if flag == 2:
                l2 = None
            else:
                l2 = l2.next
        elif l1.val > l2.val:
            if flag == 1:
                temp = None
            else:
                temp = l1.next
            l1.next = l2.next
            l2.next = l1
            l1 = temp
            if flag == 2:
                l2 = None
            else:
                l2 = l2.next
    return l


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l = mergeTwoLists(l1, l2)

while l != None:
    print(l.val)
    l = l.next
