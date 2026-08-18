class Solution:
    def trap(self, height: List[int]) -> int:
        #u take l,r and keep interating until r is >= l
        #then from l to r u substract abs(l and l+1) until u reach r 
        #min(height[l], height[r]) - height[i])
        pre = [0] * len(height)
        suf = [0] * len(height)
        res = 0
        cur_suf_max,cur_pre_max = -1,-1
        for i in range(len(height)):
            cur_pre_max = max(cur_pre_max,height[i])
            pre[i] = (cur_pre_max)
        for i in range(len(height)-1,-1,-1):
            cur_suf_max = max(cur_suf_max,height[i])
            suf[i] = (cur_suf_max)
        for i in range(len(height)):
            res += (min(pre[i],suf[i])-height[i])
        return (res)
            
