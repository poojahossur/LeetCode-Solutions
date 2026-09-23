class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        maxi = float('-inf')

        for i in nums:
            sum += i
            maxi = max(sum,maxi)

            if sum < 0:
                sum = 0
        return maxi