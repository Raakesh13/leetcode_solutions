class graph:
    def __init__(self):
        self.adjList = {}
        self.adjMatrix = [[]]

    def insertEdge(self, v1, v2, e):
        if v1 not in self.adjList:
            self.adjList[v1] = [[v2, e]]
            if v2 not in self.adjList:
                self.adjList[v2] = [[v1, e]]
            else:
                self.adjList[v2].append([v1, e])

        else:
            self.adjList[v1].append([v2, e])
            if v2 not in self.adjList:
                self.adjList[v2] = [[v1, e]]
            else:
                self.adjList[v2].append([v1, e])

    def dijkstra(self, start):
        visited = [False]*len(self.adjList)
        import math
        shortestPath = [math.inf]*len(self.adjList)
        shortestPath[start] = 0
        queue = [start]
        while queue:
            current = queue.pop()
            visited[current] = True
            for i in self.adjList[current]:
                if visited[i[0]]:
                    continue
                to = i[0]
                w = i[1]
                currentWeight = shortestPath[current] + i[1]
                if currentWeight < shortestPath[i[0]]:
                    shortestPath[i[0]] = currentWeight
                    queue.insert(0, i[0])
        return shortestPath


if __name__ == "__main__":
    ob = graph()
    ob.insertEdge(8, 0, 4)
    ob.insertEdge(8, 4, 8)
    ob.insertEdge(0, 1, 3)
    ob.insertEdge(0, 3, 2)
    ob.insertEdge(3, 2, 6)
    ob.insertEdge(3, 4, 1)
    ob.insertEdge(1, 7, 4)
    ob.insertEdge(7, 2, 2)
    ob.insertEdge(2, 5, 1)
    ob.insertEdge(5, 6, 8)

    print(ob.adjList)
    print()
    print(ob.dijkstra(6))
