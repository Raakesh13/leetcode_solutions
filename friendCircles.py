class Solution:
    def findCircleNum(self, M):
        count = 0
        visited = set()
        l = len(M)
        for i in range(l):
            if i not in visited:
                count += 1
                self.dfs(i, M, visited)

        return count

    def dfs(self, node, M, visited):
        for i, j in enumerate(M[node]):
            if j and i not in visited:
                visited.add(i)
                self.dfs(i, M, visited)


M = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
ob = Solution()
print(ob.findCircleNum(M))
