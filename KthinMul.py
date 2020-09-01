class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        low, high = 1, m * n
        while low < high:
            mid = (low + high) // 2
            # find n - smaller
            curr = 0
            j = 1
            for r in range(m, 0, -1):
                while j <= n and r * j <= mid:
                    j += 1
                    print(j, end=" ")
                print('***')
                curr += j-1
                print(curr)
            if curr < k:
                low = mid + 1
            else:
                high = mid
        return low


ob = Solution()
print(ob.findKthNumber(3, 3, 5))
