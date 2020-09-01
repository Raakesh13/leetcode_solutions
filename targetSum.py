class Solution:
    def findTargetSumWays(self, nums, S):
        import collections
        dp = [collections.defaultdict(int) for _ in range(len(nums) + 1)]
        dp[0][0] = 1
        for i, v in enumerate(nums):
            for curSum, cnt in dp[i].items():
                dp[i + 1][curSum + v] += cnt
                dp[i + 1][curSum - v] += cnt
        return dp[-1][S]


nums = [1, 1, 1, 1, 1]
S = 3

ob = Solution()
print(ob.findTargetSumWays(nums, S))
