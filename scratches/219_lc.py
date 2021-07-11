class Solution:
    def containsNearbyDuplicate(self,nums,k):
        dic = {}
        # for index,value in enumerate(nums):
        #     if value in dic and index - dic[value]<=k:
        #         return True
        #     else:
        #         dic[value] = index
        #
        # return False
        for index,value in enumerate(nums):
            if value not in dic:
                dic[value] = index
            else:
                if index - dic[value] <= k:
                    return True
                else:
                    dic[value] = index


        return False




nums = [1,2,3,1]

k=2


yz = Solution()

print(yz.containsNearbyDuplicate(nums,k))

