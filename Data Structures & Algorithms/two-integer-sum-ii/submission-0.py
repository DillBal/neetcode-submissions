class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = []
        
        while (numbers[left] + numbers[right]) != target:
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            if (numbers[left] + numbers[right]) < target:
                left += 1

        result.append(left + 1)
        result.append(right + 1)
        
        return result

