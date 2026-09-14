class Solution(object):

    def rotate(self, nums, k):

        n = len(nums)
        k %= n

        nums[:n-k] = reversed(nums[:n-k])
        nums[n-k:] = reversed(nums[n-k:])
        nums[:] = reversed(nums)

        return nums