class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        
        #         solution = []
        
        
#         # sort list to allow for use of two pointers with sum
#         nums.sort()
#         print(nums)
        
#         for i, n in enumerate(nums):
        
#             # print(i,n)
#             # start on first index
#             # left pointer set to next number
#             # right pointer set to last number
#             if n > 0:
#                 break

#             if i > 0 and n == nums[i - 1]:
#                 continue
            
#             l = i + 1
#             r = len(nums) - 1
#             print(l, r)
            
#             while(l < r):
                
#                 # if sum of left and right is greater than 0
#                 sum = nums[i] + nums[l] + nums[r]
                
#                 print(nums[i], nums[l], nums[r], sum)
                
#                 if sum < 0:
#                     l += 1
#                 elif sum > 0:
#                     r -= 1
#                 else:
#                     solution.append([nums[i], nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1
            
#         print(solution)
#         return solution
            
           
            
            # if first, left, right pointer sum to 0 append to solution list
            