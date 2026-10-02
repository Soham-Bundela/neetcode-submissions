class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict()
        res = []

        for x in nums:
            count[x] = count.get(x,0) + 1

        count = dict(sorted(count.items(),key = lambda item: item[1],reverse = True))

        for y in count:
            if k == 0:
                return res
            res.append(y)
            k -= 1
    
        return res