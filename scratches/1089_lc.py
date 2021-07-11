class Solution:
    def duplicateZeros(self, arr):
        i = 0
        n = len(arr)
        while i < n:
            if arr[i] != 0:
                i+=1
            elif arr[i] ==0:
                arr.pop()
                arr.insert(i,0)
                i+=1
                i+=1




        return arr


arr = [0,0,0]

yz = Solution()

print(yz.duplicateZeros(arr))