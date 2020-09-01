class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict
        adj = defaultdict()
        indegree = [0] * numCourses
        for i, j in prerequisites:
            if j in adj:
                adj[j].append(i)
                indegree[i] += 1
            else:
                adj[j] = [i]
                indegree[i] += 1

        st = [i for i in range(numCourses) if indegree[i] == 0]
        queue = st
        count = 0
        while queue:
            i = queue.pop()
            for j in adj[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)
            count += 1
        return count == numCourses


numCourses = 2
prerequisites = [[1, 0]]

ob = Solution()
print(ob.canFinish(numCourses, prerequisites))
