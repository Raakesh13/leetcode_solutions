class Solution:
    def leastBricks(self, wall):
        sumCount = {}
        for i in wall:
            _sum = 0
            for j in range(len(i)-1):
                _sum = _sum + i[j]
                if _sum not in sumCount:
                    sumCount[j] = 1
                else:
                    sumCount[j] += 1
        res = 0
        for i in sumCount:
            if res < sumCount[i]:
                res = sumCount[i]
        print(res)
        return res


inp = [[1, 2, 2, 1],
       [3, 1, 2],
       [1, 3, 2],
       [2, 4],
       [3, 1, 2],
       [1, 3, 1, 1]]


ob = Solution()
print(ob.leastBricks(inp))
