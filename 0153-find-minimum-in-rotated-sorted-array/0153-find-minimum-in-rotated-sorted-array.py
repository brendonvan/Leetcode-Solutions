class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        curr_min = float("inf")
        
        while start < end:
            # find middle
            mid = (start + end) // 2
            # grab current min
            curr_min = min(curr_min, nums[mid])
            
            # if mid is greater than end that means min number is on the right side of mid
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        return min(curr_min, nums[start])