class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur_lst = []
        def dfs(i):
            if i >= len(nums):
                res.append(cur_lst.copy())
                return
            cur_lst.append(nums[i])
            dfs(i+1)
            cur_lst.pop()
            dfs(i+1)
        dfs(0)
        return res



        