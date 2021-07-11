class Solution(object):
    def longestCommonPrefix(self, strs):
        if "" in strs:
            return ""
        if len(strs) == 0:
            return ""
        else:
            min_index = float("inf")
            for str in strs:
                min_index = min(min_index,len(str))

            result = ""
            for i in range(1,min_index+1):

                prefix = strs[0][:i]
                for str in strs:
                    if str[:i] != prefix:
                        return result
                result = prefix

            return result




strs = ["flower","flow","flight"]


#strs = ["aca","cba"]

yz = Solution()

print(yz.longestCommonPrefix(strs))

# mapped = list(zip(*strs))
#
# print(mapped)
#
# result = ""
#
# for n in mapped:
#     if len(set(n)) ==1:
#         result += n[0]
#     else:
#         break
#
# print(result)

