# def twoSum(arr, target):
#     temp_arr = sorted(arr)
#     i = 0
#     while i < len(temp_arr)-1 and temp_arr[i] <= target:
#         j = i+1

#         while j < len(temp_arr) and temp_arr[j] <= target:

#             if temp_arr[i]+temp_arr[j] == target:
#                 return sorted([arr.index(temp_arr[i]), arr.index(temp_arr[j])])
#             elif arr[i]+arr[j] > target:
#                 break
#             j += 1
#         i += 1


def twoSum(arr, target):
    i = 0
    while i < len(arr)-1:
        if target-arr[i] in arr[i+1:]:
            if arr[i] == target-arr[i]:
                return [i, arr[i+1:].index(target-arr[i])+i+1]
            else:
                return [i, arr.index(target-arr[i])]
        i += 1


a = [-1, -2, -3, -4, -5]
t = -8

print(twoSum(a, t))
