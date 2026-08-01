class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()#-4,-1,-1,0,1,2
        for i in range(len(nums)):
            cur_num = nums[i]
            x = i+1
            y = len(nums) - 1
            while x < y:
                if (cur_num + nums[x] + nums[y]) == 0:
                    ans.append([cur_num,nums[x],nums[y]])
                    x += 1
                    y -= 1
                if (cur_num + nums[x] + nums[y]) < 0:
                    x += 1
                if (cur_num + nums[x] + nums[y]) > 0:
                    y -= 1
        ans = set(tuple(x) for x in ans)
        return list(ans)
        
        