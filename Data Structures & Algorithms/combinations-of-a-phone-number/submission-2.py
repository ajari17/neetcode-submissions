class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = []
        def dfs(cur,i):
            #base case
            if i == len(digits):
                res.append(cur)
                return
            for char in mapp[digits[i]]:
                    dfs(cur+char,i+1)
        dfs("",0)
        return res

