class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            minHeight = min(height[left], height[right])
            currentArea = minHeight * (right - left)
            area = max(area, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area
