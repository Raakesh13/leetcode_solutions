class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx = 0
        heights.append(0)
        stack = []
        i = 0
        while i < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                h = heights[index]
                w = i
                if stack:
                    w = i - stack[-1] - 1
                mx = max(mx, h * w)

        return mx
