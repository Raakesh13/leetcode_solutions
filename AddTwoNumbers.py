class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
ls = [l1, l2]
numbers = []


for l in ls:
    count = 0
    num = 0
    while l.next:
        num = num + l.val*10**count
        l = l.next
        count += 1
    num = num + l.val*10**count
    numbers.append(num)
print(numbers)
num3 = sum(numbers)
count = len(str(num3))
l = ListNode(num3 % 10)
prev = l
num3 //= 10
while num3 > 0:
    # print(num3)
    n = ListNode(num3 % 10)
    num3 //= 10
    prev.next = n
    prev = n

while l.next:
    print(l.val)
    l = l.next
print(l.val)
