class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #-4,-1,-1,0,1,2
        for i in range(len(nums)):
            cur_num = nums[i]
            left = i+1
            right = len(nums) - 1
            while left < right:
                summ = nums[left] + cur_num + nums[right]
                if nums[left] + cur_num + nums[right] == 0:
                    res.append([nums[left],cur_num,nums[right]])
                    left += 1
                    right -= 1
                elif summ < 0:
                    left += 1
                else:
                    right -= 1
        fin = set()
        for ans in res:
            fin.add(tuple(ans))
        return list(fin)