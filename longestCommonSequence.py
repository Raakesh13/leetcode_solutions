class Solution:
    # seq = ""

    def lcs(self, s1, s2, m, n):
        # if i == 0 or j == 0:
        #     return 0
        # elif s1[i-1] == s2[j-1]:  # and i+1 == j:
        #     self.seq = s1[i-1]+self.seq
        #     return 1 + self.lcs(s1, s2, i-1, j-1)
        # else:
        #     return max(self.lcs(s1, s2, i, j-1), self.lcs(s1, s2, i-1, j))
        dp = [[None] * (n+1)for i in range(m+1)]
        for i in dp:
            print(i)
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                for k in dp:
                    print(k)
        return dp[m][n]


s1 = "Rakesh"
s2 = "Umesh"

ob = Solution()

print(ob.lcs(s1, s2, len(s1), len(s2)))
# print(ob.seq)
