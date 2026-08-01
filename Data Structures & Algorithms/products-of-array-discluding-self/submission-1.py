class Solution:
    def productExceptSelf(self, nums: List[int]):
        ans = []
        for i in range(len(nums)):
            t = 1
            for j in range(len(nums)):
                #print(i,t)
                if(j == i):
                    continue
                else:
                    t = t * nums[j]
            ans.append(t)
        return ans
        