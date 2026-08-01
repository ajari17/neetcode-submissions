class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_len = 0
        left = 0
        max_freq = 0
        for r in range(len(s)):
            #update the freq of the cur char
            counts[s[r]] = counts.get(s[r], 0) + 1
            #update the max freqency
            max_freq = max(max_freq, counts[s[r]]) #basically if we look at eg 1 after the first iteration the most freq element frequcy is 1
            #make sure the window is valid
            while ((r - left) + 1 - max_freq) > k:
                counts[s[left]] -= 1 #reduce freq of the left chars
                left += 1 #shift the left pointer forward
            max_len = max(max_len, ((r - left) + 1))
            #WINDOW formula: right - left + 1
        return max_len
            
        