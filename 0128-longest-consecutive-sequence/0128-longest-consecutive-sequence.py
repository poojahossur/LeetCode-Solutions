class Solution(object):
    def longestConsecutive(self, nums):
        num = set(nums)
        start = 0
        count = 0
        for i in num:
            if i-1 not in num:
                start = i
                length = 1
                
                while start + 1 in num :
                    start += 1
                    length += 1

                count = max(count,length) 
        return count

