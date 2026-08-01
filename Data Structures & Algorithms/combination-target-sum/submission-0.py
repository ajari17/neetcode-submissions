class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(cur_sum,i):
            if i >= len(nums) or cur_sum > target:
                return
            if cur_sum == target:
                if cur.copy() not in res:
                    res.append(cur.copy())
            cur.append(nums[i])
            dfs(cur_sum + nums[i], i)
            cur.pop()
            dfs(cur_sum, i+1)
        dfs(0,0)   
        return (res)