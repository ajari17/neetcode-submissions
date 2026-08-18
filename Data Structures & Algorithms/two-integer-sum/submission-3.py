class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:   
        mapp = {}
        for index,val in enumerate(nums):
            print(index,val)
            dif = target - val
            if dif in mapp:
                return [mapp[dif],index]
            mapp[val] = index
