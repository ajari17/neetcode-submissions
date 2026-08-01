class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for string in strs:
            cur_count = [0] * 26 #manual counter
            for char in string:
                cur_count[ord(char) - ord("a")] += 1
            res[tuple(cur_count)].append(string)
        return list(res.values())
        
