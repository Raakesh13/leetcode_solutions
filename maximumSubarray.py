def maxSubArray(nums):
    maxSum = 0
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        for i in range(len(nums)):
            for j in range(i+1):
                print(nums[j:i+1])
                if sum(nums[j:i]) > maxSum:
                    maxSum = sum(nums[j:i])
    return maxSum


a = [-2, 1]
print(maxSubArray(a))
