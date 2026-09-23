class Solution(object):
    def maxProfit(self, nums):
        mini = nums[0]
        profit = 0
        for i in range(len(nums)):
            mini = min (mini , nums[i])
            cost = nums[i] - mini 
            profit = max(cost , profit)

        return profit

        