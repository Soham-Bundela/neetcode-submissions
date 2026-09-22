class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = dict()
        for i in range(len(nums)):
            if nums[i] not in dictionary:
                dictionary[nums[i]] = 1
            else:
                return True
        return False