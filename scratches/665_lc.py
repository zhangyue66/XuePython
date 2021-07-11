class Solution:
    def checkPossibility(self, nums):
        one_num = nums[:]
        two_num = nums[:]
        print(one_num)
        print(two_num)

        counter = 0

        for i in range(len(nums)-1):
            if nums[i] >nums[i+1]:

                one_num[i] = nums[i+1]
                nums.append(0)
                two_num[i+1] = nums[i]
                break
        print(one_num)
        print(two_num)
        if one_num == sorted(one_num) or two_num==sorted(two_num):
            return True
        else:
            return False


        # one, two = nums[:], nums[:]
        # for i in range(len(nums) - 1):
        #     if nums[i] > nums[i + 1]:
        #         one[i] = nums[i + 1]
        #         two[i + 1] = nums[i]
        #         break
        # return one == sorted(one) or two == sorted(two)
nums =  [3,4,2,5]

yz = Solution()

print(yz.checkPossibility(nums))