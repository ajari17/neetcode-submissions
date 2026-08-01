class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {},{}
        # initialize the counts of chars in t
        for char in t:
            countT[char] = 1 + countT.get(char,0)#if u find exsisting chars get the amt or add 0 by default (for the .get funtion)
        have, need = 0, len(countT)
        res, reslen = [-1,-1], float("inf")#set 2 default pointer and a max length 
        left = 0
        for right in range(len(s)):
            char = s[right]
            window[s[right]] = 1 + window.get(s[right], 0)
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (right-left+1) < reslen:
                    res = [left,right]
                    reslen = right-left+1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        if reslen == float("infinity"):
            return ""
        else:
            l,r = res
            return s[l:r+1]
                