class Solution:
    def findMin(self, nums) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if nums[right] > nums[0]:
            return nums[0]        
        
        while right >= left:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


# S = Solution()
# nums = [4,5,6,7,0,1,2]
# nums = [3,4,5,1,2]
# nums = [2, 1]
# print(S.findMin(nums))