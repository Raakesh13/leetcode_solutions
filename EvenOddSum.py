class Solution:
    def evenOddSum(self, arr, number):
        sum = 0
        if number == 1:
            for i in arr[::2]:
                print(i)
                sum += i
        elif number == 2:
            for i in arr[1::2]:
                print(i)

                sum += i
        return sum


arr = [1, 2, 3, 4, 5, 6, 7]
ob = Solution()
res = ob.evenOddSum(arr, 2)
print(res)
