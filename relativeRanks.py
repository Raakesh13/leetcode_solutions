class Solution:
    def findRelativeRanks(self, nums):
        _nums = sorted(nums, reverse=True)
        D = dict()
        L = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(len(nums)):
            if i < 3:
                D[_nums[i]] = L[i]
            else:
                D[_nums[i]] = str(i+1)
        for j in range(len(nums)):
            nums[j] = D[nums[j]]
        return nums


nums = [5, 4, 3, 1, 2]
ob = Solution()
print(ob.findRelativeRanks(nums))
