class Solution:
    def findMin(self, nums) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        def is_ok(x):
            return nums[0] > nums[x]

        def bisect(ng, ok):
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if is_ok(mid):
                    ok = mid
                else:
                    ng = mid
            return ok

        n = len(nums)
        bi = bisect(-1, n)
        return nums[bi]


# S = Solution()
# nums = [4,5,6,7,0,1,2]
# nums = [3,4,5,1,2]
# nums = [2, 1]
# nums = [11,13,15,17]
# nums = [1]
# print(S.findMin(nums))