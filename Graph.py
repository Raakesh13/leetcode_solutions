class graph():
    def __init__(self):
        self.adjacancyList = {}
        self.adjacancyMatrix = []
        self.addedVertices = {}

    def insertEdge(self, v1, v2):
        if v1 not in self.adjacancyList:
            self.adjacancyList[v1] = [v2]
            if v2 not in self.adjacancyList:
                self.adjacancyList[v2] = [v1]
            else:
                self.adjacancyList[v2].append(v1)
            self.addedVertices[v1] = False
        else:
            self.adjacancyList[v1].append(v2)
            if v2 not in self.adjacancyList:
                self.adjacancyList[v2] = [v1]
            else:
                self.adjacancyList[v2].append(v1)

        # self.adjacancyList[v2].append(v1)

    def isVisited(self, v1):
        if self.addedVertices[v1]:
            return True
        else:
            self.addedVertices[v1] = True
            return False

    def dfs(self, root):
        visited = [False]*len(self.adjacancyList)
        self._dfs(root, visited)

    def _dfs(self, root, visited):
        if visited[root-1]:
            return
        visited[root-1] = True
        neighbours = self.adjacancyList[root]
        print(root, neighbours)
        for next in neighbours:
            self._dfs(next, visited)

    def bfs(self, root):
        visited = [False]*len(self.adjacancyList)
        queue = [root]
        while queue:
            current = queue.pop()
            if visited[current-1]:
                continue
            visited[current-1] = True
            print(current)
            queue = self.adjacancyList[current][::-1] + queue

    def topoogicalSort(self):
        indegree = {node: 0 for node in self.adjacancyList}
        for node in self.adjacancyList:
            for neighbours in self.adjacancyList[node]:
                indegree[node] += 1

        nodeList = []
        for node in self.adjacancyList:
            if indegree[node] == 0:
                nodeList.append(node)

        topsorted = []

        while nodeList:
            node = nodeList.pop()
            topsorted.append(node)

            for neighbours in self.adjacancyList[node]:
                indegree[neighbours] -= 1
                if indegree[neighbours] == 0:
                    topsorted.append(neighbours)

        if len(topsorted) == len(self.adjacancyList):
            print(topsorted)


if __name__ == "__main__":
    ob = graph()
    ob.insertEdge(1, 2)
    ob.insertEdge(2, 3)
    ob.insertEdge(2, 4)
    ob.insertEdge(3, 5)
    ob.insertEdge(3, 6)
    ob.insertEdge(3, 7)
    ob.insertEdge(6, 7)
    ob.insertEdge(7, 5)

    # print(len(ob.adjacancyList))
    ob.dfs(list(ob.adjacancyList.keys())[0])

    ob.bfs(list(ob.adjacancyList.keys())[0])

    ob.topoogicalSort()
