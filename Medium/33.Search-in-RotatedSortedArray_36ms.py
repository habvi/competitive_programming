# Runtime: 36 ms, faster than 92.52% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 14.7 MB, less than 56.60% of Python3 online submissions for Search in Rotated Sorted Array.

class Solution:
    def search(self, nums, target) -> int:
        from bisect import bisect
        def is_ok(x):
            if nums[0] > nums[x]:
                return True
            else:
                return False
        def bisect2(ng, ok):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if is_ok(mid):
                    ok = mid
                else:
                    ng = mid
            return ok
        
        n = len(nums)
        if n == 2:
            bi = 0 if nums[0] < nums[1] else 1
        else:
            bi = bisect2(-1, n)

        r = bisect(nums, target, lo=bi, hi=n)
        if nums[r - 1] == target:
            return r - 1

        l  = bisect(nums, target, lo=0, hi=bi)
        if nums[l - 1] == target:
            return l - 1
        return -1


# S = Solution()
# nums = [1, 2, 4]
# nums = [5, 0, 2, 4]
# nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [20, 50, 1, 5, 8, 14]
# nums = [3, 1]
# nums = [3, 5, 1]
# target = 3
# print(S.search(nums, target))