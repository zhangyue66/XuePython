class Solution:
    def mySqrt(self, x: int):
        if x < 2:
            return x
        else:
            left = 1
            right = x // 2

            while left <= right:
                mid = left + (right-left)//2
                if mid **2 > x:
                    right = mid -1
                else:
                    left = mid + 1
            return left -1






yz =Solution()

x =   18

print(yz.mySqrt(x))