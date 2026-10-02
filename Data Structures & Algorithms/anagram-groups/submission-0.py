class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            sorted_value = ''.join(sorted(strs[i]))
            hashmap[sorted_value].append(strs[i])

        return list(hashmap.values())