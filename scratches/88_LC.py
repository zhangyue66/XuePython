class Solution:
    def merge(self, nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m>0 and n>0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[n+m-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


nums1 = [1,1,6,7,8,0,0,0]
m = 5
nums2 = [1,2,9]
n = 3

yz = Solution()

yz.merge(nums1,m,nums2,n)

print(nums1)