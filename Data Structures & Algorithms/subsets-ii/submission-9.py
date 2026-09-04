class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res,cur = [],[]
        nums.sort()#sort to skip past same elements
        def dfs(i):
            if i >= len(nums):
                cur_copy = cur.copy()
                if cur_copy not in res:#check if its alr in res
                    res.append(cur_copy)
                    return
            cur.append(nums[i])#add
            dfs(i+1)#dfs
            cur.pop()#pop
            while i < len(nums)-1 and nums[i] == nums[i+1]:#while loop to keep going until next new element
                i += 1
            dfs(i+1)#dfs 
        
        dfs(0)
        return res
                    
            
        