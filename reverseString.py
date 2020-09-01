class Solution:
    def reverseString(self, s):
        if len(s) > 1:
            l = 0
            r = len(s)-1
            self._reverseString(s, l, r)
        else:
            s[0], s[-1] = s[-1], s[0]

    def _reverseString(self, s, l, r):
        if l < r:
            s[l], s[r] = s[r], s[l]
            self._reverseString(s, l+1, r-1)
            print(s[l], s[r])


s = ["h", "e", "l", "l", "o"]

ob = Solution()
ob.reverseString(s)
print(s)
