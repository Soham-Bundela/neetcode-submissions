class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashmap = defaultdict()
        
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        nums[:hashmap.get(0,0)] = [0] * hashmap.get(0,0)
        nums[hashmap.get(0,0):hashmap.get(0,0)+hashmap.get(1,0)] = [1] * hashmap.get(1,0)
        nums[hashmap.get(0,0)+hashmap.get(1,0):] = [2] * hashmap.get(2,0)