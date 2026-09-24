class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        prefix = 0
        freq = {0: 1}

        for i in nums:
            prefix += i

            if prefix - k in freq:
                count += freq[prefix - k]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count