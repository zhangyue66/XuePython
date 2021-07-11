class Solution:
    def maxArea(self, height):
        res = -float("inf")  #area of the rectanglar
        left = 0
        right = len(height)-1
        while left < right:
            area = (right-left)*min(height[left],height[right])
            if area > res:
                res = area
            if height[left]<= height[right]:
                left += 1
            else:
                right -= 1

        return res








yz = Solution()
height = [1,8,6,2,5,4,8,3,7]

print(yz.maxArea(height))