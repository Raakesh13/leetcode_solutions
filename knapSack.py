class Solution:
    def knapSack(self, W, wt, val, n):
        if n == 0 or W == 0:
            return 0

        if wt[n-1] > W:
            return self.knapSack(W, wt, val, n-1)

        else:
            return max(val[n-1]+self.knapSack(W-wt[n-1], wt, val, n-1), self.knapSack(W, wt, val, n-1))

    def knapSackDP(self, W, wt, val, n):
        dp = [[0 for i in range(W+1)]for i in range(n+1)]

        for i in dp:
            print(i)
        print()
        for i in range(n+1):
            for j in range(W+1):

                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif wt[i-1] <= j:
                    dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])

                else:
                    dp[i][j] = dp[i-1][j]
        for i in dp:
            print(i)
        return dp[n][W]

    def knapSackMemo(self, W, wt, val, n, memo):
        if n == 0 or W == 0:
            return 0

        if (W, n) in memo:
            return memo[(W, n)]

        ans = 0

        if wt[n-1] > W:
            ans = self.knapSackMemo(W, wt, val, n-1, memo)

        else:
            ans = max(val[n-1]+self.knapSackMemo(W-wt[n-1], wt,
                                                 val, n-1, memo), self.knapSackMemo(W, wt, val, n-1, memo))

        memo[(W, n)] = ans
        print(memo)
        return ans


W = 50
wt = [10, 20, 30]
val = [60, 100, 120]
n = 3

ob = Solution()
memo = {}
print(ob.knapSackMemo(W, wt, val, n, memo))
