class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midArr = l + (r - l) // 2
            if nums[midArr] > target:
                r = midArr - 1

            elif nums[midArr] < target:
                l = midArr + 1

            else:
                return midArr
            
        return -1