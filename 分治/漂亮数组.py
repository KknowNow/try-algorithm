class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        start = nums[0]
        end = nums[r]
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                ans = mid
                break
            if target >= nums[0]:
                if nums[mid] < target and nums[mid] >= nums[0]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target and nums[mid] < nums[0]:
                    r = mid - 1
                else:
                    l = mid + 1
        return ans
