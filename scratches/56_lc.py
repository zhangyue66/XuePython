class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        else:
            intervals.sort(key = lambda x : x[0])

            ans = []

            for interval in intervals:
                if len(ans) == 0 or ans[-1][1] < interval[0]:
                    ans.append(interval)
                else:
                    ans[-1][1] = max(ans[-1][1],interval[1])

            return ans






yz = Solution()

intervals = [[1,3],[2,6],[8,10],[15,18]]

print(yz.merge(intervals))