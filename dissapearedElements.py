class Solution:
    def findDisappearedNumbers(self, nums):
        l = len(nums)
        for i in range(1, l+1):
            if i in nums:
                while i in nums:
                    nums.remove(i)

            else:
                nums.append(i)
        return nums


nums = [4, 3, 2, 7, 8, 2, 3, 1]
ob = Solution()
print(ob.findDisappearedNumbers(nums))
