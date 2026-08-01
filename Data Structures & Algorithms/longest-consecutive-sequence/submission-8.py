class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in nums:
                cur_max = 0
                while (n+cur_max + 1) in nums:
                    cur_max += 1
                longest = max(cur_max, longest)
        return longest + 1


        """O(nlogn) 
        if(len(nums) == 0):
            return 0
        new = list(sorted(set((nums))))
        count = 0
        maximum = 0
        #print(new)
        for i in range(len(new) - 1):
            cur = new[i]
            #print(cur, "index:",i)
            if cur + 1 == new[i+1]:
                count += 1
               # print("consec",count)

            elif cur + 1 != new[i+1]:
                maximum = max(maximum,count)
                count = 0
        
        return max(maximum,count)+1
        """
            