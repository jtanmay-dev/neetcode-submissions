class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #2 pointer solution

        res = []
        nums.sort()

        for i, a in enumerate(nums):

            if a > 0:
                break # rest all numbers are positive, they will not sum to zero
            
            if i > 0 and a == nums[i - 1]:
                continue #duplicate as last number
            
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

                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1
        return res
