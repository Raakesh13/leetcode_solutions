def search(arr, key):
    if len(arr) == 1 and arr[0] == key:
        return True
    else:
        return binarysearch(arr, key, 0, len(arr)-1)


def binarysearch(arr, val, l, r):
    m = (l+r)//2
    if arr[m] == val:
        return True
    elif l >= r:
        return False
    elif arr[m] > val:
        return binarysearch(arr, val, l, m-1)
    elif arr[m] < val:
        return binarysearch(arr, val, m+1, r)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(search(arr, 4))
