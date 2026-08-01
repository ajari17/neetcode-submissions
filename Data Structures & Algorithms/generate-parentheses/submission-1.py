class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openn, close, cur_str):
            if len(cur_str) == 2 * n:
                res.append(cur_str)
                return

            if openn < n:
                dfs(openn + 1, close, cur_str + "(")

            if close < openn:
                dfs(openn, close + 1, cur_str + ")")
                
        dfs(0,0,"")
        return res
            
