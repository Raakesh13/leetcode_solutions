def removeDuplicates(nums):
    index = 0
    for i in range(len(nums)):
        if nums[index] != nums[i]:
            index += 1
            nums[index] = nums[i]

    return list(nums)


a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates(a))
# for i in :
#     print()
