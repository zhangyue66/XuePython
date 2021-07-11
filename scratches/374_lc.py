# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int):
        left = 1
        right = n
        while left <= right:
            mid =(left+right)//2
            ret = guess(mid)

            if ret == 0:
                return mid
            else:
                if ret == 1:
                    right = mid-1
                if ret == -1:
                    left = mid+1

