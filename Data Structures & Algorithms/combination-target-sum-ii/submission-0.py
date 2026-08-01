class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,cur = [],[]
        candidates.sort()
        def dfs(cur_sum,i):
            if cur_sum == target:
                sum_rn = cur.copy() 
                if sum_rn not in res:
                    res.append(sum_rn)
            if cur_sum > target or i >= len(candidates):
                return 
            cur.append(candidates[i])
            dfs(cur_sum + candidates[i], i + 1)
            cur.pop()
            while (i + 1 < len(candidates)) and (candidates[i] == candidates[i+1]):
                i += 1
            dfs(cur_sum, i + 1)
            
        dfs(0,0)
        return res
            