class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        midArray = int(len(nums)/2)
        print("end of array", len(nums) - 1)

        if target not in nums:
            return -1

        if target < nums[midArray]:
            print("true")
            for i in range(0, midArray):
                if nums[i] == target:
                    return i

        elif target > nums[midArray]:
            for i in range(midArray, len(nums)):
                print("iR", nums[i])
                if nums[i] == target:
                    return i
        
        elif target == nums[midArray]:
            return midArray
        
        return -1
            