class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Go through list and add each number together with no repeats
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]