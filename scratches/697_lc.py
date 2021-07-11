
class Solution:
    def findShortestSubArray(self, nums):
        if len(nums) ==0:
            return 0
        else:
            freq = {}
            for num in nums:
                freq[num] = nums.count(num)
            keys = []
            values = []
            for key,value in freq.items():
                values.append(value)
                keys.append(key)
            degree = max(values)

            cand = []
            for i in range(len(values)):
                if values[i] == degree:
                    cand.append(keys[i])

            answer = []
            for j in range(len(cand)):
                indices = [i for i,x in enumerate(nums) if x ==cand[j]]
                left = indices[0]
                right = indices[len(indices)-1]
                distance = right - left+1
                answer.append(distance)





            return min(answer)


yz = Solution()

nums = []

print(yz.findShortestSubArray(nums))
