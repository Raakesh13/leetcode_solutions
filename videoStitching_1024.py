class Solution:
    def videoStitching(self, clips, T):
        max_val = T

        steps = 0
        while max_val > 0:
            steps = steps+1
            min_val = T

            i = 0
            while i < len(clips):
                if clips[i][0] <= max_val and max_val <= clips[i][1]:
                    min_val = min(min_val, clips[i][0])
                    clips.pop(i)
                else:
                    i = i+1
                print(clips, i)
            if min_val == max_val:
                return -1

            max_val = min_val
        return steps


clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
T = 10

ob = Solution()
print(ob.videoStitching(clips, T))
