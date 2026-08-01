class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1,1,2,8 --> prefix
        #48,24,6,1 --> post fix
        prefix = 1
        ans = [1] * len(nums)
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]

        post = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= post
            post *= nums[i]
        return ans
        
        