class Solution:
    def decodeString(self, s):
        stack = []
        nums = "123456789"
        l = len(s)
        for i in range(l):
            if s[i] == "]":
                temp = stack.pop
                print(temp)
                # while stack and (temp not in nums):
                #     temp = stack.pop
                #     print(temp)
                # # temp = stack.pop()
                # # print(temp)
            else:
                stack.append(s[i])
                print(stack)


s = "3[a]2[bc]"
ob = Solution()
ob.decodeString(s)
