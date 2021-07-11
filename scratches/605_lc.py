class Solution:
    def canPlaceFlowers(self, flowerbed,n):
        if flowerbed == [0]:
            return True
        else:
            count = 0
            for i in range(len(flowerbed)):
                if i ==0 and flowerbed[i] ==0 and flowerbed[i+1] ==0:
                    flowerbed[i] =1
                    count += 1
                if i < len(flowerbed)-1 and flowerbed[i] ==0 and flowerbed[i-1] ==0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
                if i == len(flowerbed)-1 and flowerbed[i-1] ==0 and flowerbed[i] ==0:
                    flowerbed[i] =1
                    count += 1

            if count >= n:
                return True
            else:
                return False



yz = Solution()

flowerbed = [0]
n = 1

print(yz.canPlaceFlowers(flowerbed,n))
