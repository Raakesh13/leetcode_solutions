class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        # dic = set(wordList)
        # if endWord not in dic:
        #     return 0
        # import collections
        # q = collections.deque()
        # q.append(beginWord)
        # count = 1
        # while q:
        #     size = len(q)
        #     count += 1
        #     for _ in range(size):
        #         w = q.popleft()
        #         for i in range(len(w)):
        #             for c in range(ord('a'), ord('z')+1):
        #                 nw = w[:i]+chr(c)+w[i+1:]
        #                 print(nw)
        #                 if nw == endWord:
        #                     return count
        #                 if nw in dic:
        #                     q.append(nw)
        #                     dic.remove(nw)
        # return 0

        adjList = self.buildGraph([beginWord]+wordList)
        print(adjList)
        return self.dfs(beginWord, endWord, adjList)

    def buildGraph(self, wordList):
        adjList = {i: set() for i in wordList}
        adjList
        l = len(adjList)
        for i in range(l):
            for j in range(l):
                if self.diffWord(wordList[i], wordList[j]):
                    adjList[wordList[i]].add(wordList[j])
                    adjList[wordList[j]].add(wordList[i])
        return adjList

    def diffWord(self, word1, word2):
        if len(word1) != len(word2) or word1 == word2:
            return False
        else:
            l = len(word1)
            count = 0
            for i in range(l):
                if word1[i] != word2[i]:
                    count += 1
                    if count > 1:
                        return False
            if count == 1:
                return True

    def dfs(self, root, endWord, adjacancyList):
        visited = {i: False for i in adjacancyList}
        import math
        count = math.inf
        count = self._dfs(root, endWord, visited, adjacancyList, count)
        print(count)

    def _dfs(self, root, endWord, visited, adjacancyList, count):
        if root == endWord:
            return 0
        if visited[root]:
            import math
            return math.inf
        visited[root] = True
        neighbours = adjacancyList[root]
        print(root, neighbours)
        for next in neighbours:
            print(next)
            count = min(count, self._dfs(
                next, endWord, visited, adjacancyList, count) + 1)
            return count


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

ob = Solution()
print(ob.ladderLength(beginWord, endWord, wordList))
