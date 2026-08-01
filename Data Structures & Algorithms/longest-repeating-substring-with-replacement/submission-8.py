class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        max_len = 0
        left = 0
        max_freq = 0
        
        for right in range(len(s)):
            # 1. Add the incoming character to our window counts
            counts[s[right]] = counts.get(s[right], 0) + 1
            
            # 2. Track the highest frequency of any single character in the current window
            max_freq = max(max_freq, counts[s[right]])
            
            # 3. If (window size - max_freq) > k, we have exceeded our budget. Shrink from left.
            if (right - left + 1) - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                
            # 4. Update our absolute maximum window length seen so far
            max_len = max(max_len, right - left + 1)
            
        return max_len