class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        single = set(nums)

        for num in single:
            if num - 1 not in single:
                length = 1
                while num + length in single:
                    length += 1
                longest = max(longest,length)

        return longest