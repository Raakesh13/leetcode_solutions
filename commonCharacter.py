class Solution:
    def commonChars(self, A):
        if len(A) == 0:
            return A
        elif len(A) == 1:
            return list(A[0])
        else:
            from collections import Counter
            count = Counter(A[0])
            for i in A[1:]:
                for j in list(i):
                    if j in count:
                        count[j] += 1

            res = []
            l = len(A)
            count = [[k, v] for k, v in count.items()]
            print(count)
            for i in count:
                print(i[1], l)
                if i[1] >= l:
                    while i[1] and i[1]-l >= 0:
                        res.append(i[0])
                        i[1] = i[1]-l

            return res


inp = ["cool"]

ob = Solution()
print(ob.commonChars(inp))
