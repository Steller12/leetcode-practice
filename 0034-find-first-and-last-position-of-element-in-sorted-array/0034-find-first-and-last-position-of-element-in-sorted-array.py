class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            low, high = 0, len(nums) - 1
            bound = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid  
                    high = mid - 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound

        def upper_bound(nums, target):
            low, high = 0, len(nums) - 1
            bound = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    bound = mid  
                    low = mid + 1  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return bound

        return [lower_bound(nums, target), upper_bound(nums, target)]
