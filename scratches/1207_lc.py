class Solution:
    def uniqueOccurrences(self, arr):
        dict = {}

        for ar in arr:
            if ar not in dict:
                dict[ar] = 1
            else:
                dict[ar] += 1
        check = []
        for key,value in dict.items():
            if value not in check:
                check.append(value)
            else:
                return False

        return True


arr = [1,2]
yz = Solution()
print(yz.uniqueOccurrences(arr))