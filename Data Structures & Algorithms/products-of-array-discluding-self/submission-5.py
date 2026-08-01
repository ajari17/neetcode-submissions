class Solution:
    def productExceptSelf(self, nums: List[int]):
        if 0 in nums == False:
            total = 1
            for i in range(len(nums)):
                total *= nums[i]

            ans = []
            for i in range(len(nums)):
                ans.append(int((total/nums[i])))

            return ans
        else:
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
  
        