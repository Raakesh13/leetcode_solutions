# # import os
# # import sys

# # #
# # # Complete the equalStacks function below.
# # #


# # def equalStacks(h1, h2, h3):
# #     noOfCylinders = 0
# #     while True:
# #         if sum(h1) == sum(h2) == sum(h3):
# #             return noOfCylinders
# #         else:
# #             if sum(h1) > sum(h2) and sum(h1) > sum(h3):
# #                 h1 = h1[1:]
# #             elif sum(h2) > sum(h1) and sum(h2) > sum(h3):
# #                 h2 = h2[1:]
# #             elif sum(h3) > sum(h2) and sum(h3) > sum(h2):
# #                 h3 = h3[1:]
# #             noOfCylinders += 1


# # if __name__ == '__main__':

# #     h1 = [3, 2, 1, 1, 1]
# #     h2 = [4, 3, 2]
# #     h3 = [1, 1, 4, 1]

# #     result = equalStacks(h1, h2, h3)

# #     print(result)

# def check(arr, s, e):
#     m = len(arr[s:e])//2
#     if s == m and sum(arr[:m]) != sum(arr[m+1:]):
#         return "NO"
#     elif s == m and sum(arr[:m]) == sum(arr[m+1:]):
#         return "YES"
#     elif sum(arr[:m]) == sum(arr[m+1:]):
#         return "YES"
#     elif sum(arr[:m]) < sum(arr[m+1:]):
#         return check(arr, m, e)
#     elif sum(arr[:m]) > sum(arr[m+1:]):
#         return check(arr, s, m)

#     return "NO"


# def balancedSums(arr):
#     if len(arr) == 1:
#         return "YES"
#     elif len(arr) == 2:
#         return "NO"
#     else:
#         return check(arr, 0, len(arr)-1)
#     #     m = len(arr)//2
#     #     visited = []
#     #     while (m != 0 or m+2 > len(arr)) and m not in visited:
#     #         if sum(arr[0:m]) == sum(arr[m+1:]):
#     #             return "YES"
#     #         elif sum(arr[0:m]) < sum(arr[m+1:]):
#     #             visited.append(m)
#     #             m += 1
#     #         elif sum(arr[0:m]) > sum(arr[m+1:]):
#     #             visited.append(m)
#     #             m -= 1
#     # return "NO"


# if __name__ == '__main__':

#     arr = [1, 2, 3]
#     print(balancedSums(arr))


def median(arr):
    arr.sort()
    l = len(arr)
    m = l//2
    if len(arr) % 2 == 0:
        return (arr[m]+arr[m+1])/2
    else:
        return arr[m]


def activityNotifications(expenditure, d):
    count = 0
    for i in range(d, len(expenditure)):
        if expenditure[i] >= 2*median(expenditure[:i]):
            count += 1

    return count


if __name__ == '__main__':
    arr = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    print(activityNotifications(arr, 5))
