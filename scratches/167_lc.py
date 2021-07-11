class Solution:
    # def twoSum(self,numbers,target):
    #     for i in range(len(numbers)-1):
    #         for j in range(i+1,len(numbers)):
    #             if numbers[i] + numbers[j] == target:
    #                 return [i+1,j+1]
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1

        while i < j:
            if numbers[i]+numbers[j] == target:
                return [i+1,j+1]
            elif numbers[i]+numbers[j] > target:
                j -= 1
            else:
                i += 1
        return None






numbers = [2,7,11,15]
target = 101

yz = Solution()

print(yz.twoSum(numbers,target))