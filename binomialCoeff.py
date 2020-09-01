class Solution:
    def binomialCoeff(self, n, k):
        # if k == 0 or k == n:
        #     return 1
        # return self.binomialCoeff(n-1, k-1)+self.binomialCoeff(n-1, k)
        dp = [[0 for j in range(n+1)]for i in range(n+1)]

        for i in range(n+1):
            for j in range(n+1):
                if j == 0 or j == i:
                    dp[i][j] = 1

                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        for i in dp:
            print(i)
        return dp[n]


ob = Solution()
print(ob.binomialCoeff(4, 2))
