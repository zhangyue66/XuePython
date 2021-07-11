class Solution:
    def groupAnagrams(self, strs):
        ans = []

        # array to save all valid dictionary
        str_dict = []

        for str in strs:
            if not str and [""] not in ans:
                ans.append([""])

            dict = {}

            for letter in str:
                if letter not in dict:
                    dict[letter] = 1
                else:
                    dict[letter] += 1

            if dict not in str_dict:
                str_dict.append(dict)
                ans.append([str])
            else:
                id = str_dict.index(dict)
                ans[id].append(str)

        return ans



yz = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(yz.groupAnagrams(strs))