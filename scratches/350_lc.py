class Solution:
    def intersect(self, nums1,nums2):
        i,j = 0,0
        ans = []

        if len(nums1) == 0 or len(nums2) == 0:
            return[]

        else:
            nums1.sort()
            nums2.sort()

            while i<len(nums1) and j < len(nums2):
                if nums1[i] < nums2[j]:
                    i += 1
                    continue
                if nums1[i] > nums2[j]:
                    j += 1
                    continue

                if nums1[i] == nums2[j]:
                    ans.append(nums1[i])
                    i += 1
                    j += 1
                    continue

            return ans



nums1 = [4,9,5,99,999,99999,9996765,9546563456]
nums2 = [9,4,9,8,4]

yz = Solution()

print(yz.intersect(nums1,nums2))