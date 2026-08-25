class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        #-4,-1,-1,0,1,2
        for i in range(n):
            cur_num = nums[i]
            l = i+1
            r = n-1
            while l < r:
                summ = nums[l] + nums[r] + cur_num
                if summ == 0:
                    res.add((nums[l],nums[r],cur_num)) 
                    l += 1
                    r -= 1
                elif summ < 0: 
                    l += 1
                else:
                    r -= 1
        return list(res)           
       