class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        occ = (Counter(nums))
        print(occ)
        for key,val in occ.items():
            if occ[key] >= 2:
                return key
        return -1