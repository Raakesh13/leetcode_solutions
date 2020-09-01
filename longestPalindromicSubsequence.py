class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [[0 for i in range(l)] for i in range(l)]

        for i in range(l):
            print(dp[i])

        for i in range(l):
            dp[i][i] = 1

        for i in range(l):
            print(dp[i])
        print()
        for index in range(2, l+1):
            for i in range(l-index+1):
                j = i+index-1
                if s[i] == s[j] and index == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2

                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])

                for k in range(l):
                    print(dp[k])
        return dp[0][l-1]


s = "MAM"
ob = Solution()
print(ob.longestPalindromeSubseq(s))
