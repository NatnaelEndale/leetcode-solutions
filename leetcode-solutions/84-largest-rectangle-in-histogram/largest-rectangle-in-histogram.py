class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                stk_h, stk_i = stack.pop()
                max_area = max(max_area, stk_h * (i - stk_i))
                start = stk_i

            stack.append((h, start))

        while stack:
            stk_h, stk_i = stack.pop()
            max_area = max(max_area, stk_h * (n - stk_i))

        return max_area

        