class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        #Time Complexity: O(n^2)
        #Space Complexity: O(1)
        """
        maximum_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                if min(height[i], height[j]) * (j-i) > maximum_area:
                    maximum_area = min(height[i], height[j]) * (j-i)
        return maximum_area
        """

        #Time Complexity: O(n)
        #Space Complexity: O(1)
        left = 0
        right = len(height) - 1
        maximum_area = 0
        h, w = 0, 0
        while left != right:
            if height[left] <= height[right]:
                h = height[left]
                w = right - left
                if h*w > maximum_area:
                    maximum_area = h*w
                left += 1
            else:
                h = height[right]
                w = right - left
                if h*w > maximum_area:
                    maximum_area = h*w
                right -= 1
        return maximum_area
