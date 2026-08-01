class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        
        # Step 1: Calculate Prefix Products
        # ans[i] will contain the product of all elements to the left of i
        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Calculate Suffix Products on the fly
        # Multiply the existing prefix in ans[i] by the product of elements to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]
            
        return ans
