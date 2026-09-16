class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sum = (n * (n + 1))//2
        s2 = 0
        for i in nums:
            s2 += i
           
        return (sum - s2)