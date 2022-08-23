

class Solution:
   def maxSubArray(self, nums):



        max_sum_until_i = max_sum= nums[0]




        for i, num in enumerate(nums[1:],start=1):
            print(max_sum_until_i)
            max_sum_until_i = max(max_sum_until_i+num, num)
            max_sum = max(max_sum,max_sum_until_i)
        return max_sum


test=Solution()


test.maxSubArray([5,4,-1,7,8])