class Solution:
    def accountsMerge(self, accounts):
        if len(accounts) == 0:
            return []
        else:
            res = []
            graph = {}
            mailToName = {}
            for account in accounts:
                name = account[0]
                l = len(account[1:])
                for i in range(1, l+1):
                    emailId = account[i]
                    mailToName[emailId] = name
                    if emailId not in graph:
                        graph[emailId] = {}
                    if i == 1:
                        continue
                    prev = account[i-1]
                    graph[prev] = emailId
                    graph[emailId] = prev

            visited = set()
            for email in mailToName.keys():
                name = mailToName.get(email)
                emails = []
                if email not in visited:
                    visited.add(emailId)
                    self.dfs(emails, email, graph, visited)
                    emails.sort()
                    emails.insert(0, name)
                    res.append(emails)

            return res

    def dfs(self, emails, email, graph, visited):
        emails.append(email)
        if len(graph[email]) == 0:
            return
        for neighbour in graph[email]:
            if neighbour not in visited:
                visited.add(neighbour)
                self.dfs(emails, neighbour, graph, visited)


accounts = [["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com",
                                                                      "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]]


ob = Solution()
print(ob.accountsMerge(accounts))
