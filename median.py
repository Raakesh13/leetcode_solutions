def median(List):
    if len(List) % 2 == 0:
        return (List[len(List)//2-1]+List[len(List)//2])/2
    else:
        return List[len(List)//2]


def findMedian(list1, list2):
    if len(list1) == len(list2) == 2:
        print(list1, list2)
        print(1)
        med = (max(list1[0], list2[0])+min(list1[1], list2[1]))
        print(med)
        return med/2
    elif median(list1) == median(list2):
        print(2)
        return median(list1)
    elif median(list1) > median(list2):
        print(3)
        return findMedian(list1[:len(list1)//2], list2[len(list2)//2:])
    else:
        print(4)
        return findMedian(list2[:len(list2)//2], list1[len(list1)//2:])


med = findMedian([1, 5, 7, 9], [2, 3, 4, 8])
print(med)
