class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        
        # sort list to allow for use of two pointers with sum
        nums.sort()
        print(nums)
        [-4, -1, -1, 0, 1, 2]
        
        for i, n in enumerate(nums):
            # if there's no negative numbers it can't sum to 0
            if n > 0:
                break

            # if not first index and same number as prev num on list continue
            if i > 0 and n == nums[i - 1]:
                continue
            
            # left pointer set to next number
            # right pointer set to last number
            l = i + 1
            r = len(nums) - 1
            
            while(l < r):
                # if sum of left and right is greater than 0
                # print(nums[i], nums[l], nums[r], sum)
                sum = nums[i] + nums[l] + nums[r]
                
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    solution.append([nums[i], nums[l], nums[r]])
                    
                    # check others in this starting index
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        # print(solution)
        return solution
            
          
            