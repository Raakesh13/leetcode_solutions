#A = list(map(int, input().split()))
#pivot = int(input())

A = [5, 1, 2, 6, 4, 7]
index = 3
pivot = A[index]
for i in range(len(A)):
    if pivot < A[i]:
        A[index], A[i] = A[i], A[index]

print(A)
