class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])

        return self.binarySearch(matrix, target, 0, (m*n)-1, n)

    def binarySearch(self, matrix, target, l, r, cols):
        if l <= r:
            m = (l+r)//2
            row = m//cols
            col = m % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                return self.binarySearch(matrix, target, l, m-1, cols)
            else:
                return self.binarySearch(matrix, target, m+1, r, cols)
        else:
            return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 3
ob = Solution()
print(ob.searchMatrix(matrix, target))
