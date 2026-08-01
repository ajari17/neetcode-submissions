class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cur,res = [],[]
        def dfs(i):
            if i >= len(nums):
                subset = cur.copy()
                subset = sorted(subset)
                if not subset in res:
                    res.append(subset)
                return
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return res
